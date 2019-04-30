from turtle import *

speed(-1)
n=-1
mamau=True
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

while mamau:
    n += 1
    color(colors[n])
    fillcolor(colors[n])
    
    begin_fill()

    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    
    end_fill()
    if n==5:
        mamau=False
    

mainloop()
