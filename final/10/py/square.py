import turtle

class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.speed(0)
        self.draw()

    def draw(self, color="black"):
        self.t.clear()
        self.t.fillcolor(color)
        self.t.goto(self.x, self.y)
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(self.size)
            self.t.left(90)
        self.t.end_fill()

    def move_up(self):
        if self.y < 200:
            self.y += 10
            self.draw()

    def move_down(self):
        if self.y > -200:
            self.y -= 10
            self.draw()

    def inc_size(self):
        self.size += 5
        self.draw()

    def dec_size(self):
        if self.size > 5:
            self.size -= 5
            self.draw()
