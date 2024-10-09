import pandas

url_sheet_um = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2013"
url_sheet_dois = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2014"
data_um = pandas.read_csv(url_sheet_um)
data_dois = pandas.read_csv(url_sheet_dois)

print(data_um,data_dois)