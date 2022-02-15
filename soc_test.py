import turtle as tt
import random as rd

com = tt.Turtle()
com.shape('turtle')
user = tt.Turtle()
user.shape('circle')

user.penup()
user.goto(-150, 30)

user.pendown()
user.left(90)
user.forward(120)
user.right(90)
user.forward(300)
user.right(90)
user.forward(120)

user.penup()
user.goto(0, -100)

com.penup()
com.goto(0, 30)
com.right(90)

user.speed(9)
com.speed(0)

com_lst = ['f','l','r']

s =  tt.textinput("패널티킥", "f, l, r 입력")
com_ac = rd.choice(com_lst)
if com_ac == 'f':
    com.goto(0, 30)
if com_ac == 'l':
    com.goto(-100, 30)
if com_ac == 'r':
    com.goto(100, 30)

if s == 'f':
    user.goto(0, 50)
if s == 'l':
    user.goto(-100, 50)
if s == 'r':
    user.goto(100, 50)
