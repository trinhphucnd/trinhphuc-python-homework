from turtle import *
speed(-1)
count = 0

# draw H
for i in range(4):
    right(90)
    forward(100)
    goto(0,count-50)
    left(90)
    forward(50)
    goto(50,count)
    right(90)
    forward(100)

    # draw E

    penup()
    goto(60,count-50)
    pendown()
    forward(50)
    left(90)
    forward(50) 
    penup()
    goto(60,count-75)
    pendown()
    forward(50)
    penup()
    goto(60,count-50)
    pendown()
    forward(50)

    # draw ll
    penup()
    setpos(120,count)
    pendown()
    right(90)
    forward(100)
    penup()
    setpos(130,count)
    pendown()
    forward(100)

    # draw o 
    penup()
    setpos(140,count-75)
    pendown()
    circle(25)
    

    penup()
    goto(0,count+150)
    pendown()
    left(90)

    count += 150


    
    

mainloop()