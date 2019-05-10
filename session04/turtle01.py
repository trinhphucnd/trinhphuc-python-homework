from turtle import *

speed(-1)
color('blue')
shape('triangle')
count = 0
loop = True
while loop :
    for i in range (4):
        forward(80)
        left(90)
    for i in range (4):
        forward(80)
        right(90)

    left(180)

    for i in range (4):
        forward(80)
        left(90)
    for i in range (4):
        forward(80)
        right(90)

    right(15)
    
    count +=1

    if count == 6:
        break 

mainloop()