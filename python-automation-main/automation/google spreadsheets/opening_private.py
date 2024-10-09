import gspread

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("weather_private")

worksheet = spreadsheet.get_worksheet(0)

data = worksheet.get_all_records()
print(data)

worksheet = spreadsheet.worksheet("2013")
data = worksheet.get_all_records()
print(data)