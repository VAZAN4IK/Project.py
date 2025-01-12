from turtle import *
from random import randint

# Функція для малювання треку
def track():
    begin_fill()
    color('black')
    penup()
    goto(-250, 75)
    pendown()
    forward(500)
    right(90)
    forward(150)
    right(90)
    forward(500)
    right(90)
    forward(150)
    right(90)
    end_fill()
    goto(-250, 0)
    penup()
    color('white')
    width(4)
    forward(25)
    for _ in range(10):
        pendown()
        forward(20)
        penup()
        forward(30)

track()

# Створюємо обєкти машинок
c1 = Turtle()
c2 = Turtle()

# Задаємо значення обєктів
c1.shape('square')
c1.color('red')
c1.width(5)
c1.penup()
c1.goto(-250, 45)

c2.shape('square')
c2.color('blue')
c2.width(5)
c2.penup()
c2.goto(-250, -45)

# Функція для ручного руху першої машинки
def trotle():
    c1.forward(20)

# Реєструємо клавішу для руху
scr = c1.getscreen()
scr.listen()
scr.onkey(trotle, 'Up')

# Основний цикл гри
while c1.xcor() < 250 and c2.xcor() < 250:
    c2.forward(randint(1       , 3))

# Визначення переможця
if c1.xcor() >= 250:
    print("Червона машинка перемогла!")
elif c2.xcor() >= 250:
    print("Синя машинка перемогла!")
