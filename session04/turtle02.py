from turtle import *

speed (-1)
color('blue')
shape('circle')
right(140)

n = 100
while True :

    
    for i in range (4):
        forward(n)
        right(90)
        
    right(10)
    n -= 2
    if n == 0:
        break

mainloop()