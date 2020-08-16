from projects import Project
import time
import xlwt
import xlrd
from xlwt import Workbook
import os.path
from datetime import date

class Sheet:

    def __init__(self, name):
        self.name = name
        self.main_list = []
        self.project_name_row = []
        self.project_dates_col = []
        self.nrow = 0
        self.ncol = 0


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
        self.project_dates_col = sheet1.col_values(0)

        data_for_the_day = []
        #self.project_name_row = sheet1.row_values(0)

        for i in range(1,ncol):
            project_obj = Project(sheet1.cell_value(0,i))
            for j in range(1, nrow):
                date = sheet1.cell_value(j,0)
                words = sheet1.cell_value(j, i)
                project_obj.list_of_occurences.append([date, words])

            self.main_list.append(project_obj)


    def update_file(self, day, month, year, new_project, new_words):

        today = day + " " + month

        temp_project = Project(new_project)

        dates_from_list_of_dates = []
        for dates in self.project_dates_col:
            if dates != " ":
                dates_from_list_of_dates.append(dates)

        index_proj = 9999
        project_exists = False
        project_date_exists = False
        index_date = 9999

        # checks if project project exists and get its index in the main list
        for index, project in enumerate(self.main_list):
            if project.get_name() == new_project:
                index_proj = index
                project_exists = True

        if project_exists == True:
            for date_proj, data_pair in enumerate(self.main_list[index_proj].list_of_occurences):
                if data_pair[0] == today:
                    index_date = date_proj
                    project_date_exists = True

            if project_date_exists == True:
                self.main_list[index_proj].list_of_occurences[index_date][1] = new_words
                pass

            else:
                self.main_list[index_proj].list_of_occurences.append([today, new_words])
                pass


        elif project_exists == False:
            temp_project.list_of_occurences.append([today, new_words])
            self.main_list.append(temp_project)

        # Once all checked are done, re-write the sheet with updated info
        wb = xlwt.Workbook()
        sheet1 = wb.add_sheet(month+year)

        counter_rows = len(self.project_dates_col)
        counter_col = 0
        index_of_date = 9999
        date_exists_in_file = False



        for projects in self.main_list:
            counter_col += 1
            sheet1.write(0, counter_col, projects.get_name())
            for date_words_pair in range(len(projects.list_of_occurences)):


                for index_of_row, date_of_proj in enumerate(dates_from_list_of_dates):
                    if date_of_proj == projects.list_of_occurences[date_words_pair][0]:
                        index_of_date = index_of_row
                        date_exists_in_file = True
                        print(index_of_date)

                if date_exists_in_file == True:
                    try:
                        sheet1.write(index_of_date, 0, projects.list_of_occurences[date_words_pair][0])
                        sheet1.write(index_of_date, counter_col, projects.list_of_occurences[date_words_pair][1])
                    except:
                        sheet1.write(index_of_date, counter_col, projects.list_of_occurences[date_words_pair][1])


                else:
                    counter_rows +=1
                    sheet1.write(counter_rows,0,projects.list_of_occurences[date_words_pair][0])
                    sheet1.write(counter_rows,counter_col,projects.list_of_occurences[date_words_pair][1])
                    dates_from_list_of_dates.append(projects.list_of_occurences[date_words_pair][0])




        wb.save("PTS_" + month + "_" + year + ".xls")
