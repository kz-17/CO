import turtle

class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.speed(0)
        self.draw()

    def draw(self):
        self.pen.goto(self.x, self.y)
        self.pen.begin_fill()
        for _ in range(4):
            self.pen.forward(self.size)
            self.pen.left(90)
        self.pen.end_fill()

    def erase(self):
        self.pen.clear()

    def move_up(self):
        if self.y < 250:
            self.erase()
            self.y += 10
            self.draw()

    def move_down(self):
        if self.y > -250:
            self.erase()
            self.y -= 10
            self.draw()

# 模擬 SquareGame 的執行
def start_game():
    screen = turtle.Screen()
    screen.setup(600, 600)
    
    # 建立正方形物件 (對應 Square.new)
    sq = Square(0, 0, 30)
    
    # 綁定鍵盤事件 (對應 SquareGame.run 中的 key processing)
    screen.listen()
    screen.onkey(sq.move_up, "Up")
    screen.onkey(sq.move_down, "Down")
    
    print("遊戲開始：使用方向鍵 Up/Down 移動正方形")
    screen.mainloop()

if __name__ == "__main__":
    start_game()
