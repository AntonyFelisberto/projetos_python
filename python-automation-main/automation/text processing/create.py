
file = open("file.txt", "w")
file.write("text\n")
file.write("news\n")

content = """
    First

    second
"""
file.write(content)
file.close()

with open("files.txt", "w") as f: # with fecha os arquivos automaticamente
    f.write(" amount ")
    f.write(" amount ")
    f.write(" amount ")