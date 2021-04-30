import pygame
from pprint import pprint
import copy
pygame.init()

class Color:
    BLACK   =   (0,     0,      0)
    WHITE   =   (255,   255,    255)
    BLUE    =   (0,     0,      255)
    RED     =   (255,   0,      0)
    GREENLIGHT = '#A7DA48'
    GREENDARKER = '#8ECD39'

class Snake:
    def __init__(self, boxSize):
        self.x = boxSize + 5
        self.y = boxSize
        self.nowDirection = [0,0]

    def setDirection(self, inputDirection):
        # 반대쪽 방향을 누르지 않았을 경우 !
        plusX = self.nowDirection[0] + inputDirection[0]
        plusY = self.nowDirection[1] + inputDirection[1]
        if plusX != 0 or plusY != 0:
            self.nowDirection = inputDirection
class Box:
    def __init__(self):
        self.font = pygame.font.Font('Gulim.ttf',30)  #폰트 설정
        # text = self.font.render("글자출력",True,(28,0,0))  #텍스트가 표시된 Surface 를 만듬
    def renderText(self,screen):
        background.blit(screen.text,(870,20))              #화면에 표시 


    

class Board:
    def __init__(self, boxSize, boardSize):
        self.width = boardSize[0]
        self.height = boardSize[1]
        self.boxSize = boxSize
        # self.board = [[1 if i == 0 or i == self.height-1 else 0] * self.width for i in range(self.width)] * self.height
        self.board = [[0] * self.width for _ in range(self.width) ] * self.height
        for y,row in enumerate(self.board):
            for x,col in enumerate(row):
                if x == 0 or y == 0 or x == len(row)-1 or y == len(self.board)-1:
                    self.board[y][x] = 1

        
    def drawBoard(self, screen):
        for y,row in enumerate(self.board): 
            for x,col in enumerate(row):
                nowColor = Color.BLACK
                # 테두리를 까맣게 칠함
                if col == 1:
                    nowColor = Color.BLACK
                # 홀수일 경우 연한녹색
                elif (y+x) % 2 == 0:
                    nowColor = Color.GREENLIGHT
                # 짝수일 경우 진한 녹색
                else: 
                    nowColor = Color.GREENDARKER
                #보드를 그림
                pygame.draw.rect(screen, nowColor,
                [x * self.boxSize, y * self.boxSize, self.boxSize, self.boxSize])


class Game:
    def __init__(self, boxSize, boardSize):
        self.board = Board(boxSize, boardSize)
        self.snake = Snake(boxSize)

    def drawGame(self, screen):
        self.board.drawBoard(screen)
        # self.snake.drawSnake(screen)

    def setSnakeDirection(self,direction):
        self.snake.setDirection(direction)

def main():
    boxSize, boardSize = 30, [25,25] 
    screenSize = [boardSize[0] * boxSize, boardSize[1] * boxSize]
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Title")
    pygame.font.SysFont()

    done = False
    clock = pygame.time.Clock()
    game = Game(boxSize, boardSize)
    prevKeyDown =  0

    # test = Box()

    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dome = True
            if event.type == pygame.KEYDOWN and event.key != prevKeyDown:
                if event.key == pygame.MOUSEBUTTONDOWN != 0:
                    game.setSnakeDirection([-1,0])
                elif event.key == pygame.K_RIGHT:
                    game.setSnakeDirection([1,0])
                elif event.key == pygame.K_
                    game.setSnakeDirection([0,-1])
                elif event.key == pygame.K_DOWN:
                    game.setSnakeDirection([0,1])
                prevKeyDown = event.key

        screen.fill(Color.WHITE)
        game.drawGame(screen)
        pygame.display.flip()
        pygame.Color()
main()