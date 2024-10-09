import gspread

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("weather_private")

worksheet = spreadsheet.worksheet("2013")

existing_column = worksheet.get_values("E5:E25")
new_column = [[round((float(i[0]) * 9/5 + 32),1)]for i in existing_column]
print(new_column)

worksheet.update("G2:G25",[["Fahrenheit"]]+new_column)
