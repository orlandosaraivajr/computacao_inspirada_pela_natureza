import pygame
import random
import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron

# Configurações do jogo
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 7
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Criação do Perceptron
X =  pd.read_pickle("./features.pkl")
y =  pd.read_pickle("./targets.pkl")
perceptron = Perceptron(max_iter=1000, random_state=43)
perceptron.fit(X, y)

def up_or_down(position_x, position_y, speed_x, speed_y):
    b = np.array([position_x, position_y, speed_x, speed_y])
    dado = np.ndarray((1,4), buffer=b,dtype=int)
    up_or_down = perceptron.predict(dado)[0]
    return up_or_down
    
# Classe para representar a bola
class Ball:
    def __init__(self):
        self.size = 20
        self.x = WIDTH // 2 - self.size // 2
        self.y = HEIGHT // 2 - self.size // 2
        self.speed_x = random.choice([-BALL_SPEED, BALL_SPEED])
        self.speed_y = random.choice([-BALL_SPEED, BALL_SPEED])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Verificar colisão com as paredes superior e inferior
        if self.y <= 0 or self.y + self.size >= HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.size, self.size))

# Classe para representar as paletas dos jogadores
class Paddle:
    def __init__(self, x):
        self.width = 15
        self.height = 100
        self.x = x
        self.y = HEIGHT // 2 - self.height // 2

    def move_up(self):
        self.y -= PADDLE_SPEED
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += PADDLE_SPEED
        if self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    ball = Ball()
    player1 = Paddle(20)
    player2 = Paddle(WIDTH - 20 - 15)

    score_player1 = 0
    score_player2 = 0

    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()

        ball.move()
        
        if player1.y + player1.width > ball.y:
            player1.move_up()
        if player1.y + player1.width < ball.y:
            player1.move_down()

        if up_or_down(ball.x, ball.y, ball.speed_x, ball.speed_y) == 1:
            player2.move_up()    
        else:
            player2.move_down()
        
        # Verificar colisão com as paletas dos jogadores
        if ball.x <= player1.x + player1.width and player1.y <= ball.y <= player1.y + player1.height:
            ball.speed_x *= -1
        elif ball.x + ball.size >= player2.x and player2.y <= ball.y <= player2.y + player2.height:
            ball.speed_x *= -1

        # Verificar se a bola atingiu uma das paredes laterais
        if ball.x <= 0:
            score_player2 += 1
            ball.__init__()  # Reiniciar a bola
        elif ball.x + ball.size >= WIDTH:
            score_player1 += 1
            ball.__init__()  # Reiniciar a bola

        screen.fill(BLACK)
        ball.draw(screen)
        player1.draw(screen)
        player2.draw(screen)

        # Renderizar os pontos dos jogadores na tela
        text_player1 = font.render(f"Player 1: {score_player1}", True, WHITE)
        text_player2 = font.render(f"Player 2: {score_player2}", True, WHITE)
        screen.blit(text_player1, (20, 20))
        screen.blit(text_player2, (WIDTH - text_player2.get_width() - 20, 20))

        # Verificar se algum jogador atingiu a pontuação máxima (por exemplo, 5)
        if score_player1 == 5:
            winner_text = font.render("Player 1 venceu!", True, WHITE)
            screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)  # Aguardar 2 segundos
            break
        elif score_player2 == 5:
            winner_text = font.render("Player 2 venceu!", True, WHITE)
            screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)  # Aguardar 2 segundos
            break

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()

if __name__ == "__main__":
    main()

