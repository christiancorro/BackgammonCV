# import pygame module in this program
import pygame
import random

from Board import Board
from Color import Color
from BoardPosition import BoardPosition
from Constants import UI_POINT_CENTERS


class BoardScene:
    def __init__(self):
        self.init()
        self.background = pygame.image.load("../data/images/UI/board.jpg")
        self.background_detecting = pygame.image.load("../data/images/UI/Detecting.jpg")
        self.background_aligning = pygame.image.load("../data/images/UI/alignTemplate.jpg")
        self.disk_w = pygame.image.load("../data/images/UI/disk_w.png").convert_alpha()
        self.disk_b = pygame.image.load("../data/images/UI/disk_b.png").convert_alpha()
        self.disk_low_confidence = pygame.image.load("../data/images/UI/disk_low_probability.png").convert_alpha()
        self.dices_w = self.loadDices("dice_w")
        self.dices_b = self.loadDices("dice_b")
        self.dices_low_confidence = self.loadDices("dice_low_probability")
        self.disk_height = self.disk_b.get_height()
        self.disk_width = self.disk_b.get_width()
        self.window_height = self.background.get_height()
        self.window_width = self.background.get_width()

        self.threshold_low_confidence = 0.6

        self.sceneClock = pygame.time.Clock()
        self.white = (255, 255, 255)
        self.points = UI_POINT_CENTERS
        self.board = Board()
        pygame.display.set_mode((self.window_width, self.window_height))

        self.update()

    def init(self):
        pygame.display.set_mode((0, 0), flags=pygame.HIDDEN)
        pygame.display.set_caption("Board")
        self.screen = pygame.display.get_surface()

    def drawDices(self):
        left_count = 0
        right_count = 0
        for i in range(min(4, len(self.board.dices))):
            # for dice in self.board.dices:
            # if random.randint(0, 1) == 0:
            # self.screen.blit(self.dices_b[i - 1], (random.randint(80, 200), 300))
            # else:
            dice = self.board.dices[i]
            diceImages = 0
            if dice.color == Color.WHITE:
                diceImages = self.dices_w
            else:
                diceImages = self.dices_b
            if dice.confidence < self.threshold_low_confidence:
                diceImages = self.dices_low_confidence
            if dice.board_position == BoardPosition.LEFT:
                left_count += 1
                self.screen.blit(diceImages[dice.id], (100 + 50 * left_count, 320))
            else:
                right_count += 1
                self.screen.blit(diceImages[dice.id], (480 + 50 * right_count, 320))

    def drawDisks(self):
        for i in range(len(self.board.points)):
            point = self.board.points[i]
            x, y = point.center
            for j in range(len(point.disks)):
                disk = point.disks[j]
                y1 = 0
                x1 = 0
                if i < 12:
                    x1 = x - self.disk_width // 2
                    y1 = y - self.disk_height * (j + 1)
                else:
                    x1 = x - self.disk_width // 2
                    y1 = y + self.disk_height * (j)
                if disk.confidence < self.threshold_low_confidence:
                    self.screen.blit(self.disk_low_confidence, (x1, y1))
                else:
                    if disk.color == Color.WHITE:
                        self.screen.blit(self.disk_w, (x1, y1))
                    else:
                        self.screen.blit(self.disk_b, (x1, y1))

    def updateBoard(self, board):
        self.board = board
        self.update()

    def reset(self):
        pygame.display.update()

    def detecting(self):
        # self.screen.fill(self.white)
        self.screen.blit(self.background_detecting, (0, 0))
        pygame.display.update()

    def alligning(self):
        # self.screen.fill(self.white)
        self.screen.blit(self.background_aligning, (0, 0))
        pygame.display.update()

    def update(self):
        # infinite loop
        # while True:

        # completely fill the surface object
        # with white colour
        self.screen.fill(self.white)

        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        self.screen.blit(self.background, (0, 0))

        self.drawDisks()
        self.drawDices()

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            # if event.type == pygame.MOUSEMOTION:
            # (mouseX, mouseY) = pygame.mouse.get_pos()
            # x = mouseX
            # y = mouseY
            # self.screen.blit(self.disk_w, (x, y))
            # if event.type == pygame.MOUSEBUTTONDOWN:

            # self.updateBoard()
            if event.type == pygame.QUIT:

                # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()

            # Draws the surface object to the screen.
        pygame.display.update()

    def loadDices(self, dice):
        dices = []
        for i in range(6):
            filename = "../data/images/UI/" + dice + "_" + str(i + 1) + ".png"
            dices.append(pygame.image.load(filename).convert_alpha())
        return dices


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((761, 668))
    # set the pygame window name
    pygame.display.set_caption("Image")
    screen = pygame.display.get_surface()
    BoardScene = BoardScene(screen)
    BoardScene.update()
