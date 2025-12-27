import pygame
import sys

# 初始化圖形環境
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 512, 256 # 模擬 Hack 螢幕解析度
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Square:
    def __init__(self, x, y, size):
        self.x, self.y = x, y
        self.size = size

    def draw(self, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))

    def inc_size(self):
        if (self.y + self.size < SCREEN_HEIGHT - 2) and (self.x + self.size < SCREEN_WIDTH - 2):
            self.size += 2

    def dec_size(self):
        if self.size > 2:
            self.size -= 2

    def move(self, direction):
        if direction == 1 and self.y > 2: # Up
            self.y -= 2
        elif direction == 2 and self.y + self.size < SCREEN_HEIGHT - 2: # Down
            self.y += 2
        elif direction == 3 and self.x > 2: # Left
            self.x -= 2
        elif direction == 4 and self.x + self.size < SCREEN_WIDTH - 2: # Right
            self.x += 2

class SquareGame:
    def __init__(self):
        self.square = Square(0, 0, 30)
        self.direction = 0 # 0=none, 1=up, 2=down, 3=left, 4=right
        self.exit = False

    def run(self):
        while not self.exit:
            screen.fill((255, 255, 255)) # 背景設為白色
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_q: self.exit = True
                    elif key == pygame.K_z: self.square.dec_size()
                    elif key == pygame.K_x: self.square.inc_size()
                    elif key == pygame.K_UP: self.direction = 1
                    elif key == pygame.K_DOWN: self.direction = 2
                    elif key == pygame.K_LEFT: self.direction = 3
                    elif key == pygame.K_RIGHT: self.direction = 4

            # 執行移動邏輯
            self.square.move(self.direction)
            
            # 繪製正方形 (黑色)
            self.square.draw((0, 0, 0))
            
            pygame.display.flip()
            clock.tick(60) # 限制運行速度

if __name__ == "__main__":
    game = SquareGame()
    game.run()
