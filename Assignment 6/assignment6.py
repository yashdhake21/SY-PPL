import turtle

bob = turtle.Turtle()

bob.color("blue","cyan")

class shape:
    def __init__(self,sides=0,length=0):
        self.sides = sides
        self.length = length

class polygon(shape):
    def info(self):
        print("A polygon is a 2D shape with straight sides")

class square(polygon):
    def show(self):
        for i in range(4):
            bob.forward(self.length)
            bob.left(90)

class triangle(polygon):
    def show(self):
        for i in range(3):
            bob.forward(self.length)
            bob.left(120)

class pentagon(polygon):
    def show(self):
        for i in range(5):
            bob.forward(self.length)
            bob.left(72)

class hexagon(polygon):
    def show(self):
        for i in range(6):
            bob.forward(self.length)
            bob.left(60)

class octagon(polygon):
    def show(self):
        for i in range(8):
            bob.forward(self.length)
            bob.left(45)

class circle(polygon):
    def show(self):
        bob.circle(self.length)

c = circle(6, 100)
c.info()
c.show()

turtle.done()