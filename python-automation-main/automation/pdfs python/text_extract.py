import fitz

with fitz.open('automation\\pdfs python\\files\\students.pdf') as pdf:
    page_one =pdf[0].get_text()
    text = ""
    for page in pdf:
        print(20*"-")
        print(page.get_text())
        text = text + page.get_text()
        print(text)
    