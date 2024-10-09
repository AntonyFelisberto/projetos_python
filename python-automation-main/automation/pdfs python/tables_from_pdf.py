import tabula

table = tabula.read_pdf("automation\\pdfs python\\files\\weather.pdf",pages=1)
print(table)
print(type(table))
print(table[0])
table[0].to_csv("output.csv",index=None)