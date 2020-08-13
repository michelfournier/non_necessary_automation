from project_hoy import Project
from day import Day
import time
import xlwt
import xlrd
from xlwt import Workbook
import os.path
from datetime import date

class Sheet:

    def __init__(self, name):
        self.name = name
        self.dico_of_days = {}


    def from_scratch(self, day, month, year, project, words):

        day1 = day + " " + month
        sheet_name = month+year

        wb = xlwt.Workbook()

        sheet1 = wb.add_sheet(sheet_name)

        sheet1.write(1,0,day1)
        sheet1.write(0,1,project)
        sheet1.write(1,1,words)


        wb.save("PTS_" + month + "_" + year + ".xls")

    def read_file(self, month, year):

        EXCEL_FILES_FOLDER = '/Users/michelfournier/Desktop/work_follow_up/'
        excel_file_path = EXCEL_FILES_FOLDER+"PTS_" + month + "_" + year + ".xls"
        loc = (excel_file_path)
        wb_r = xlrd.open_workbook(loc)

        sheet1 = wb_r.sheet_by_name(month+year)

        nrow = sheet1.nrows
        ncol = sheet1.ncols

        print(nrow)
        print(ncol)



        for i in range(1,nrow):
            day_obj = Day(sheet1.cell_value(i,0))
            for j in range(1, ncol):
                project_obj = Project(sheet1.cell_value(0, j), sheet1.cell_value(i, j))
                day_obj.list_of_projects.append(project_obj)
            self.dico_of_days[day_obj] = day_obj.get_list()

        print(nrow)
        print(ncol)
        print()

        print(self.dico_of_days)
        print()

    def update_file(self, day, month, year, new_project, new_words):

        # checking for date key, if project already exists in dico.
        # If it does, update new word count or add to dico.
        temp_obj = Project(new_project, new_words)

        temp_list = []

        for fuck in self.dico_of_days:
            if fuck.get_date() == day + " " + month:
                jim = self.dico_of_days[fuck]

                for i in jim:
                    temp_list.append(i.get_name())

                if temp_obj.get_name() in temp_list:
                    for j in range(0,len(self.dico_of_days[fuck])):
                        if self.dico_of_days[fuck][j].get_name() == temp_obj.get_name():
                            self.dico_of_days[fuck][j].set_words(new_words)
                            pass


                if not temp_obj.get_name() in temp_list:
                    self.dico_of_days[fuck] = self.dico_of_days[fuck] + [temp_obj]
                    pass


        # Once all checked are done, re-write the sheet with updated info
        wb = xlwt.Workbook()
        sheet1 = wb.add_sheet(month+year)

        counter_rows = 0
        counter_col = 0

        for i in self.dico_of_days:
            counter_rows += 1
            sheet1.write(counter_rows,0,i.get_date())
            for j in range(len(self.dico_of_days[i])):
                counter_col += 1
                sheet1.write(0,counter_col,self.dico_of_days[i][j].get_name())
                sheet1.write(counter_rows,counter_col,self.dico_of_days[i][j].get_words())


        wb.save("PTS_" + month + "_" + year + ".xls")
