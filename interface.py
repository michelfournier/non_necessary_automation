from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *

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
        self.mess_frame1 = Frame(self)
        self.mess_frame1.pack(fill=X)
        self.canvas_frame = Frame(self)
        self.canvas_frame.pack(fill=BOTH, expand=1)
        self.mess_frame = Frame(self)
        self.mess_frame.pack(fill=X)
        self.btn_frame2 = Frame(self)
        self.btn_frame2.pack(fill=X)

        # Top buttons
        self.btn_new = Button(self.btn_frame, text='New month', command=self.new_worksheet)
        self.btn_new.pack(side=LEFT)

        self.btn_load = Button(self.btn_frame, text='Open', command=self.open_file)
        self.btn_load.pack(side=LEFT)

        # Input names

        self.input_project_name = Label(self.mess_frame1, text="Project")
        self.input_project_name.pack(side=LEFT)

        self.input_words_name = Label(self.canvas_frame, text="Words")
        self.input_words_name.pack(side=LEFT)

        # input fields

        self.input_project_field = Entry(self.mess_frame1)
        self.input_project_field.pack(side=RIGHT, fill=X)

        self.input_words_field = Entry(self.canvas_frame)
        self.input_words_field.pack(side=RIGHT, fill=X)

        # bouton d'arrêt
        self.btn_exit = Button(self.btn_frame2, text='exit', command=self.destroy)
        self.btn_exit.pack()


    def new_worksheet(self):
        pass

    def open_file(self):
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