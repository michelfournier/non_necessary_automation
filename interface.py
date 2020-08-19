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
        self.words_frame.pack(fill=BOTH, expand=1)
        self.submit = Frame(self)
        self.submit.pack(fill=X)
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
        self.btn_exit = Button(self.submit, text='Submit', command=self.submit_info)
        self.btn_exit.pack()

        # bouton d'arrêt
        self.btn_exit = Button(self.stop_btn_frame, text='exit', command=self.destroy)
        self.btn_exit.pack()

        # it's own sheet object

        self.sheet = Sheet("")


    def new_worksheet(self):

        self.sheet = Sheet("NEW")

    def open_file(self):
        # get the file
        existing_file = askopenfilename(title="Select file.")

        self.sheet = Sheet("OLD")

        # call Sheet read function
        self.sheet.read_file(month, year, existing_file)

        self.display_day_accounts['text'] = "Accounts of the day\n{}".format(self.get_day_projects())


    def submit_info(self):

        new_proj = self.input_project_field.get()

        new_words = self.input_words_field.get()

        filename = asksaveasfilename()

        if self.sheet.get_sheet_name() == "NEW":
            self.sheet.from_scratch(day, month, year, new_proj, new_words, filename)

        else:
            self.sheet.update_file(day, month, year, new_proj, new_words, filename)

        # need field to go back to blank
        self.input_project_field.delete(0, END)
        self.input_words_field.delete(0, END)

        self.display_day_accounts['text'] = ""

        self.display_day_accounts['text'] = "Accounts of the month\n" \
                                            "{}".format(self.get_day_projects())

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




"""""

       # Création du canvas échiquier.
        self.canvas_echiquier = CanvasEchiquier(self.canvas_frame, 60)
        self.canvas_echiquier.pack(side=LEFT)

        # Ajout d'une étiquette d'information.
        self.messages = Label(self.mess_frame)
        self.messages.pack(anchor=CENTER)

        self.pointage = Label(self.mess_frame1)
        self.pointage.pack(anchor=CENTER)
"""

if __name__ == "__main__":
    f = Window()
    f.mainloop()
