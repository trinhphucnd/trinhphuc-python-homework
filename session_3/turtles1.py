from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

speed(0)
color(colors[3])
shape("turtle")

for i in range(6):
  forward(100)
  left(60)



color(colors[1])
for i in range (4):
  forward(100)
  left(90)


color(colors[0])
left(60)
forward(100)
right(120)
forward(100)


color(colors[2])
left(132)
forward(100)
for i in range(3):
  left(72)
  forward(100)



color(colors[4])
left(72)
forward(100)
for i in range (6):
  left(180-(900/7))
  forward(100)
mainloop()
