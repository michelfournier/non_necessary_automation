class Project:

    def __init__(self, name):
        self.name = name
        self.list_of_occurrences = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_list_data(self):
        return self.list_of_occurrences

    def total_words_month(self):
        # might need a date filter
        sum_words = 0
        for i in self.list_of_occurrences:
            try:
                sum_words += int(i[1])
            except ValueError:
                pass

        return sum_words
