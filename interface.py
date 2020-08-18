from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *
from sheet.py import Sheet

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
        self.btn_exit = Button(self.submit, text='Submit', command=self.submit)
        self.btn_exit.pack()

        # bouton d'arrêt
        self.btn_exit = Button(self.stop_btn_frame, text='exit', command=self.destroy)
        self.btn_exit.pack()

        # it's own sheet object

        self.sheet = Sheet()

        # inputs

        self.new_proj = "Entry for project"
        self.new_words = "Entry for words"


    def new_worksheet(self):
        pass

    def open_file(self):
        sheet_name = askopenfilename(title="Select file.")

        self.sheet = Sheet(sheet_name)




    def submit(self):
        pass


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