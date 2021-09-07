import pygame
import random

class Apple():
    def __init__(self, display):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.r = 10
        self.dsply = display
        self.color=(255,0,0)
        
    def show(self):
         pygame.draw.circle(self.dsply, self.color, (self.x, self.y),self.r)
    

class Snake():
    def __init__(self, display):
        self.dsply = display
        self.w = 16
        self.h = 16
        self.x = width / 2
        self.y = height / 2
        self.color = (0, 250, 0)
        self.color2 = (0, 100, 0)
        self.name = 'Bahar'
        self.score = 0
        self.speed = 3
        self.x_change = 0
        self.y_change = 0
        self.grow_dir = ''
        self.body = []


    def show(self):
        head = [self.x, self.y]
        self.body.append(head)
        pygame.draw.circle(self.dsply, self.color, [self.x, self.y], 10)
        
        if self.score < len(self.body):
            del self.body[0]
            
        for i in range(len(self.body)):
            if i % 2 == 0:
                pygame.draw.circle(self.dsply, self.color, [self.body[i][0] , self.body[i][1]], 10)
            else:
                pygame.draw.circle(self.dsply, self.color2, [self.body[i][0] , self.body[i][1]], 10)
            
        
    def move(self):
        if self.grow_dir == 'l':
            self.x -= self.speed
            
        elif self.grow_dir == 'r':
            self.x += self.speed

        elif self.grow_dir == 'u':
            self.y -= self.speed

        elif self.grow_dir == 'd':
            self.y += self.speed

        #game over
        if self.x <= 50 or self.x >= 750 or self.y <= 50 or self.y >= 650:
            self.game_over()

        #speed
        if self.score > 50:
            self.speed = 6
        elif self.score > 25:
            self.speed = 5
        elif self.score > 10:
            self.speed = 4


    def eat(self, apple_x, apple_y, r):
        if apple_x - r <= self.x <= apple_x + (1.5 * r) and apple_y - r <= self.y <= apple_y + (1.5 * r):
            self.score += 1
            return 'apple'
        
    def game_over(self):
        self.speed = 0
        font_go = pygame.font.Font('font/LATINWD.ttf', 46)
        text_go = font_go.render('Game Over!!!', True, (255, 255, 255), (0, 0, 0))
        textRect_go = text_go.get_rect()
        textRect_go.center = (width / 2 , height / 2)
        self.dsply.blit(text_go, textRect_go)
pygame.init()


if __name__ == "__main__":
    width = 800
    height = 700

    dsply = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake') 
    clock = pygame.time.Clock()
    
    snake = Snake(dsply)
    apple = Apple(dsply)
    
    # core 
    font = pygame.font.Font('font/LATINWD.ttf', 32)
    text = font.render('Score: 0', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (width // 2, 30)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    snake.grow_dir= 'l'
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    snake.grow_dir = 'r'
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    snake.grow_dir = 'u'
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    snake.grow_dir = 'd'

        result = snake.eat(apple.x, apple.y, apple.r)
        if result == 'apple':
            apple = Apple(dsply)
            text = font.render(f'Score: {snake.score}', True, (255, 255, 255))
        
        dsply.fill((0,0,0))
        dsply.blit(text, textRect)
        snake.move()
        apple.show()
        snake.show()
        pygame.display.update()
        clock.tick(30)

        if snake.score < 0:
            snake.game_over()