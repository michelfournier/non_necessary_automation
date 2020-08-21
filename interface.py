from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *
from sheet import Sheet
from datetime import date

# get today's date
today = date.today()

# get today's date in format dd YYYY Month_written
day_month_year = today.strftime("%d %Y %B")
lenght_today = len(day_month_year)

day = day_month_year[0:2]
year = day_month_year[3:7]
month = day_month_year[8:lenght_today]

today = day + " " + month


class Window(Tk):

    def __init__(self):
        super().__init__()

        self.title("Work Helper")

        # automatic sizing of the elements
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # création des différents frames de l'interface
        self.btn_frame = Frame(self)
        self.btn_frame.pack(fill=X)
        # add label frame to list ongoing day projects name from sheet.mainlist
        self.proj_list_frame = Frame(self)
        self.proj_list_frame.pack(fill=X)

        self.proj_frame = Frame(self)
        self.proj_frame.pack(fill=X)
        self.words_frame = Frame(self)
        self.words_frame.pack(fill=X)
        self.submit = Frame(self)
        self.submit.pack(fill=X)
        self.save_file_frame = Frame(self)
        self.save_file_frame.pack(fill=X)
        self.stop_btn_frame = Frame(self)
        self.stop_btn_frame.pack(fill=X)

        # Top buttons
        self.btn_new = Button(self.btn_frame, text='New month', command=self.new_worksheet)
        self.btn_new.pack(side=LEFT)

        self.btn_load = Button(self.btn_frame, text='Open', command=self.open_file)
        self.btn_load.pack(side=LEFT)

        # List of proj of the day
        self.display_day_accounts = Label(self.proj_list_frame)
        self.display_day_accounts.pack(anchor=CENTER)

        # Input names

        self.input_project_name = Label(self.proj_frame, text="Project")
        self.input_project_name.pack(side=LEFT)

        self.input_words_name = Label(self.words_frame, text="Words")
        self.input_words_name.pack(side=LEFT)

        # input fields

        self.input_project_field = Entry(self.proj_frame)
        self.input_project_field.pack(side=RIGHT, fill=X)

        self.input_words_field = Entry(self.words_frame)
        self.input_words_field.pack(side=RIGHT, fill=X)

        # submit frame
        self.btn_submit = Button(self.submit, text='Submit', command=self.submit_info)
        self.btn_submit.pack()

        # save file frame
        self.btn_save = Button(self.save_file_frame, text='Save', command=self.save_proj)
        self.btn_save.pack(side=LEFT)

        # save status
        self.save_status = Label(self.save_file_frame)
        self.save_status.pack(side=RIGHT)

        # bouton d'arrêt
        self.btn_exit = Button(self.stop_btn_frame, text='exit', command=self.destroy)
        self.btn_exit.pack()

        # it's own sheet object
        self.sheet = Sheet("")

        # stamp to check if the file changed
        self.day_total_base = 0
        self.to_save_or_not_to_save = False

        self.is_it_new = False

    def new_worksheet(self):

        self.sheet = Sheet("Jeb")
        self.is_it_new = True

    def open_file(self):
        # get the file
        existing_file = askopenfilename(title="Select file.")

        self.sheet = Sheet("Jeb")

        # call Sheet read function
        self.sheet.read_file(month, year, existing_file)

        self.display_day_accounts['text'] = "Accounts of the day\n{}".format(self.get_day_projects())

        self.day_total_base = self.sheet.total_day(today)

    def submit_info(self):

        new_proj = self.input_project_field.get()

        new_words = self.input_words_field.get()

        if self.is_it_new:
            filename = asksaveasfilename()
            self.sheet.from_scratch(day, month, year, new_proj, new_words, filename)
            self.is_it_new = False
            self.open_file()



        else:
            self.sheet.update_file(day, month, new_proj, new_words)

        # need field to go back to blank

        self.input_project_field.delete(0, END)
        self.input_words_field.delete(0, END)

        self.display_day_accounts['text'] = ""

        self.display_day_accounts['text'] = "Accounts of the month\n" \
                                            "{}".format(self.get_day_projects())

        if self.day_total_base != self.sheet.total_day(today):
            self.to_save_or_not_to_save = True

        self.get_save_status()

    def get_day_projects(self):

        long_string = ""
        proj_counter = 0
        for i in self.sheet.main_list:

            if proj_counter % 3 != 0 or proj_counter == 0:
                long_string += "{}, ".format(i.get_name())
                proj_counter += 1
            else:
                long_string += "{},\n ".format(i.get_name())
                proj_counter += 1

        return long_string

    def save_proj(self):

        filename = asksaveasfilename()

        self.sheet.save_file(day, month, year, filename)

        self.to_save_or_not_to_save = False
        self.get_save_status()

    def get_save_status(self):

        if self.to_save_or_not_to_save:

            self.save_status['text'] = "GOTTA SAVE!!  "
        else:
            self.save_status['text'] = "Nothing new here  "


if __name__ == "__main__":
    f = Window()

    f.mainloop()
