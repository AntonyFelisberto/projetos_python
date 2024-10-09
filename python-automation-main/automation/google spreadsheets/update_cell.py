import gspread

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("weather_private")

worksheet = spreadsheet.worksheet("2013")

worksheet.update("E5",-29)

worksheet.update_cell(5,5,-39)