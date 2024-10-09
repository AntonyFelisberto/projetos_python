import gspread
import re

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("weather_private")

worksheet = spreadsheet.worksheet("2013")

cell = worksheet.get_values("D5")[0][0]

cell_two = worksheet.acell("D5").value

cell_three = worksheet.find("-10")
print(cell_three.row,cell_three.column)

cell_four = worksheet.findall("-9")
print(cell_four)

for cells in cell_four:
    print(cells.row,cells.column)

reg = re.compile(r"99")
cell_re = worksheet.findall(reg)

for cells in cell_four:
    print(cells.row,cells.column)