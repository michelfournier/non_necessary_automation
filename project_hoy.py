class Project:

    def __init__(self, name, words):
        self.name = name
        self.words = words


    def add_words(self, new_words):
        self.words += new_words

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_words(self):
        return self.words

    def set_words(self, words):
        self.words = words
