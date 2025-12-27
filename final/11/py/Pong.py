import pygame
import sys

# 初始化 Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 512, 256  # 模擬 Jack 的螢幕解析度
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Bat:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.direction = 0  # 0:停, 1:左, 2:右

    def move(self):
        if self.direction == 1:
            self.x = max(0, self.x - 4)
        elif self.direction == 2:
            self.x = min(SCREEN_WIDTH - self.width, self.x + 4)

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size = 6
        self.dx, self.dy = 4, -4  # 簡化原版複雜的 setDestination 邏輯

    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # 碰撞牆壁邏輯 (模擬 wall 1, 2, 3)
        if self.x <= 0 or self.x >= SCREEN_WIDTH - self.size:
            self.dx *= -1
        if self.y <= 0:
            self.dy *= -1
        
        return 4 if self.y >= 229 else 0 # 觸碰底端區域

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))

class PongGame:
    def __init__(self):
        self.bat = Bat(230, 229, 50, 7)
        self.ball = Ball(253, 222)
        self.score = 0
        self.exit = False

    def run(self):
        while not self.exit:
            screen.fill((0, 0, 0)) # 清除畫面
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: self.bat.direction = 1
                    if event.key == pygame.K_RIGHT: self.bat.direction = 2
                    if event.key == pygame.K_ESCAPE: self.exit = True
                if event.type == pygame.KEYUP:
                    self.bat.direction = 0

            self.bat.move()
            wall = self.ball.move()

            # 碰撞偵測 (對應 moveBall 方法)
            if wall == 4:
                # 檢查球是否落在球板範圍內
                if self.bat.x <= self.ball.x <= (self.bat.x + self.bat.width):
                    self.ball.dy *= -1
                    self.score += 1
                    self.bat.width = max(10, self.bat.width - 2) # 增加難度
                else:
                    self.exit = True # Game Over

            self.bat.draw()
            self.ball.draw()
            pygame.display.flip()
            clock.tick(30) # 限制幀率

        print(f"Game Over! Final Score: {self.score}")

if __name__ == "__main__":
    game = PongGame()
    game.run()
