class Project:

    def __init__(self, name):
        self.name = name
        #self.words = words
        #self.date = date
        self.list_of_occurences = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


    def get_list_data(self):
        return self.list_of_occurences

    def total_words_month(self):
        #might need a date filter
        sum = 0
        for i in self.list_of_occurences:
            sum += i[1]
        return sum