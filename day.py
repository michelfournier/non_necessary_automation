#import projects
from datetime import date


class Day:
    def __init__(self, date):
        self.date = date
        self.list_of_projects = []
        self.list_of_proj_names = []

    def get_date(self):
        return self.date

    def get_list(self):
        return self.list_of_projects

    def get_list_len(self):
        return len(self.list_of_projects)

    #def pop_list_names(self, list1):
        #for i in range(len(list1)):
            #self.list_of_proj_names.append(list1(i).get_name())

        #return self.list_of_proj_names
