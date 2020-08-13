import time
import xlwt
from xlwt import Workbook
from sheet import Sheet
from datetime import date
import os.path

# get today's date
today = date.today()

#get today's date in format dd YYYY Month_written
day_month_year = today.strftime("%d %Y %B")
lenght_today = len(day_month_year)

day = day_month_year[0:2]
year = day_month_year[3:7]
month = day_month_year[8:lenght_today]

##########


project = input("Project : ")
words = input("Words : ")


if not os.path.isfile("PTS_" + month + "_" + year + ".xls"):

    new_sheet = Sheet("Bob")

    new_sheet.from_scratch(day, month, year, project, words)

else:

    jeb = Sheet("Jeb")

    jeb.read_file(month, year)

    jeb.update_file(day, month, year, project, words)
