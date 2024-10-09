import turtle
import random

jogador = turtle.Turtle()
jogador_dois = turtle.Turtle()

jogador.hideturtle()
jogador.shape("turtle")
jogador.color("green","green")
jogador.shapesize(2,2,2)
jogador.pensize(3)

jogador_dois.hideturtle()
jogador_dois.shape("turtle")
jogador_dois.color("blue","blue")
jogador_dois.shapesize(2,2,2)
jogador_dois.pensize(3)

jogador.penup()
jogador.goto(200,200)
jogador.pendown()
jogador.circle(40)

jogador.penup()
jogador.goto(-250,225)
jogador.showturtle()

jogador_dois.penup()
jogador_dois.goto(200,-200)
jogador_dois.pendown()
jogador_dois.circle(40)

jogador_dois.penup()
jogador_dois.goto(-250,-170)
jogador_dois.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if jogador.pos() >= (200,200):
        print("verde ganhou")
        break
    elif jogador.pos() >= (200,-200):
        print("azul ganhou")
        break
    else:
        turno = input("enter para avançar no jogo")
        turno = random.choice(dado)
        print(f"seu numero é {turno} avançou {turno*20}")
        jogador.pendown()
        jogador.forward(20*turno)

        turno_dois = input("enter para avançar no jogo")
        turno_dois = random.choice(dado)
        print(f"seu numero é {turno_dois} avançou {turno_dois*20}")
        jogador_dois.pendown()
        jogador_dois.forward(20*turno_dois)

turtle.done()