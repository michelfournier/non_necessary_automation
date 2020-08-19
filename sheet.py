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
        self.project_dates_col = []

    def get_sheet_name(self):
        return self.name

    def from_scratch(self, day, month, year, project, words, filename):

        day1 = day + " " + month
        sheet_name = month + year

        wb = xlwt.Workbook()

        sheet1 = wb.add_sheet(sheet_name)

        sheet1.write(1, 0, day1)
        sheet1.write(0, 1, project)
        sheet1.write(1, 1, words)

        wb.save(filename)

    def read_file(self, month, year, file):

        wb_r = xlrd.open_workbook(file)

        sheet1 = wb_r.sheet_by_name(month + year)

        nrow = sheet1.nrows
        ncol = sheet1.ncols
        self.project_dates_col = sheet1.col_values(0)

        for i in range(1, ncol):
            project_obj = Project(sheet1.cell_value(0, i))
            for j in range(1, nrow):
                date_row = sheet1.cell_value(j, 0)
                words = sheet1.cell_value(j, i)
                project_obj.list_of_occurrences.append([date_row, words])

            self.main_list.append(project_obj)

    def update_file(self, day, month, year, new_project, new_words, filename):

        today = day + " " + month

        temp_project = Project(new_project)

        if today not in self.project_dates_col:
            self.project_dates_col.append(today)

        index_proj = 9999
        project_exists = False
        project_date_exists = False
        index_date = 9999

        # checks if project project exists and get its index in the main list
        for index, project in enumerate(self.main_list):
            if project.get_name() == new_project:
                index_proj = index
                project_exists = True
                print(index_proj)

        if project_exists == True:
            for date_proj, data_pair in enumerate(self.main_list[index_proj].list_of_occurrences):
                print(data_pair[0])
                if data_pair[0] == today:
                    index_date = date_proj
                    project_date_exists = True
                    print(index_date)

            if project_date_exists == True:
                self.main_list[index_proj].list_of_occurrences[index_date][1] = new_words


            else:
                self.main_list[index_proj].list_of_occurrences.append([today, new_words])

        if project_exists == False:
            temp_project.list_of_occurrences.append([today, new_words])
            print(temp_project.list_of_occurrences)
            self.main_list.append(temp_project)

        # Once all checked are done, re-write the sheet with updated info

        wb = xlwt.Workbook()
        sheet1 = wb.add_sheet(month + year, cell_overwrite_ok=True)

        counter_rows = len(self.project_dates_col)
        counter_col = 0
        index_of_date = 9999
        date_exists_in_file = False

        for projects in self.main_list:
            counter_col += 1
            sheet1.write(0, counter_col, projects.get_name())
            for date_words_pair in range(len(projects.list_of_occurrences)):

                for index_of_row, date_of_proj in enumerate(self.project_dates_col):
                    if date_of_proj == projects.list_of_occurrences[date_words_pair][0]:
                        index_of_date = index_of_row
                        date_exists_in_file = True
                        print(index_of_date)

                if date_exists_in_file == True:
                    try:
                        sheet1.write(index_of_date, 0, projects.list_of_occurrences[date_words_pair][0])
                        sheet1.write(index_of_date, counter_col, projects.list_of_occurrences[date_words_pair][1])
                    except:
                        sheet1.write(index_of_date, counter_col, projects.list_of_occurrences[date_words_pair][1])


                else:
                    sheet1.write(counter_rows, 0, today)
                    sheet1.write(counter_rows, counter_col, projects.list_of_occurrences[date_words_pair][1])
                    counter_rows += 1

        # print totals for month and on-going day in the useless (0,0) cell
        total_display = str(self.total_day(today)) + "/" + str(self.total_month())
        sheet1.write(0, 0, total_display)

        # create separate sheet for PTS invoicing list of projects
        self.create_month_list(wb)

        # save file
        wb.save(filename)

    def create_month_list(self, workbook):

        projects_name = []

        for projects in self.main_list:
            projects_name.append(projects.get_name())

        projects_name.sort()

        wb = workbook
        sheet2 = wb.add_sheet("Projects of the Month")

        row_count = 0

        for names in projects_name:
            sheet2.write(row_count, 0, names + " (Original No - Match Words)")
            row_count += 1
            sheet2.write(row_count, 0, names + " (Original Repetition Words)")
            row_count += 1
            sheet2.write(row_count, 0, names + " (Original High Repetition Words)")
            row_count += 1
            sheet2.write(row_count, 0, names + " (Original Suppressed Words)")
            row_count += 1

    def total_day(self, day):

        sum_day = 0

        for projects in self.main_list:
            for pairs in range(len(projects.list_of_occurrences)):
                if projects.list_of_occurrences[pairs][0] == day:
                    try:
                        sum_day += int(projects.list_of_occurrences[pairs][1])
                    except ValueError:
                        pass

        return sum_day

    def total_month(self):

        sum_month = 0

        for projects in self.main_list:
            sum_month += projects.total_words_month()

        return sum_month
