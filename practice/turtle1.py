import turtle as t
from random import choice
colors = ['red', 'blue', 'black', 'yellow', 'orange', 'green', 'purple']

big = input('크기를 입력하세요>>')

try:
    big = int(big)

    t.penup()
    t.goto(-big/2, 0)
    t.pendown()
    for i in range(100):
        t.color(choice(colors), choice(colors))
        t.forward(big)
        t.left(181)
    t.done()
except:
    print('맞는 결과를 입력하세요')

