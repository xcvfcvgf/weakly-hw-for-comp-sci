import turtle

t = turtle.Turtle()

t.color("blue")
t.width(10)
t.speed(100)

t.penup
t.goto(0,0)
t.pendown()

def house(a,h):
  def block(a):
    for i in range(4):
      t.forward(100)
      t.right(90)
  
    t.penup()
    t.goto(0,0)
    t.pendown()
  
    t.left(45)
    t.forward(a/2)
    t.right(45)
    t.forward(a)
    t.right(135)
    t.forward(a/2)
    
  
    t.backward(a/2)
  
    t.color("blue")
    t.begin_fill()
    t.left(45)
    t.forward(a)
    t.right(45)
    t.forward(a/2)
    t.right(135)
    t.forward(a)
    t.right(45)
    t.forward(a/2)
    t.color("#102138")
    t.end_fill()
  
  
  block(a)
  
  t.penup()
  t.goto(0,0)
  t.left(45)
  t.pendown()
  
  def pyramid(a,h):
    t.color("blue")
    import math
    
    angle = math.degrees(math.atan(h / (50 * math.sqrt(2))))
    t.right(int(angle))
    side = math.sqrt(h**2 + a**2 / 2)
    t.forward(int(side))
    t.right(180-2*int(angle))
    t.forward(int(side))
    t.left(2 * (90 - int(angle)))
    
    t.begin_fill()
    t.forward(a/2)
    t.left(2*(int(angle)))
    t.forward(int(side))
    t.left((360-(2 * (90 - int(angle)))-int(angle))/2)
    t.forward(a/2)
    
    t.color("blue")
    t.end_fill()
    
    
  pyramid(a, h)

house(100, 50)
