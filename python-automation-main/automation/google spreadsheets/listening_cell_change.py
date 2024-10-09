import gspread
import time

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("weather_private")

worksheet = spreadsheet.worksheet("2013")
worksheet_two = spreadsheet.worksheet("Watch")

while True:
    value = worksheet.acell("G26").value
    time.sleep(2)
    value_two = worksheet.acell("G26").value
    if value != value_two:
        worksheet.update("A1","CHANGED")