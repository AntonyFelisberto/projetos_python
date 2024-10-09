user = {}
emails = ['myMail@tnc.com',"mails@xcs.com"]

tuplas = list(enumerate(emails))
print(tuplas)

for key in range(0,len(tuplas)):
    print("MAIL ",tuplas[key][1])
    print("MAIL ",tuplas[key])
    print("MAIL ",tuplas[1])
    user[tuplas[key]]=[input("digite o nome: "),input("digite o nivel: ")]

for key,dado in user.items():
    print("usuario ",key[0])
    print("email ",key[1])
    print("nome ",dado[0])
    print("nivel ",dado[1])