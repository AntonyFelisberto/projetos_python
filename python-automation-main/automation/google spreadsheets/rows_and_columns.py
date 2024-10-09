import gspread
import statistics

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("weather_private")

worksheet = spreadsheet.worksheet("2013")

rows = worksheet.get_values("A5:F5")
rows = worksheet.row_values(3)

colums = worksheet.get_values("C2:C25")
colums = worksheet.get_values(2)[1:]

print(rows)