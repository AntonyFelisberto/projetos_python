import gspread
import statistics

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("weather_private")

worksheet = spreadsheet.worksheet("2013")

existing_column = worksheet.get_values("G2:G25")

existing_column = [float(i[0]) for i in existing_column]

average = statistics.mean(existing_column)
worksheet.update("G26",average)