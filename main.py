import turtle as t
import random
tim = t.Turtle()

colours = ['blue','red','green','black','yellow','pink','orange']
########### Challenge 3 - Draw Shapes #######
def draw_shape(num_sides):
  angle = 360/num_sides
  for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)

for side in range(3,11):
  tim.color(random.choice(colours))
  draw_shape(side)





