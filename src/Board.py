import random
from Color import Color
from Disk import Disk
from Utils import pointInPoly
from BoardPosition import BoardPosition
import copy
import json


class Board:
    def __init__(self):
        self.bbox = []
        self.points = []
        self.dices = []

    def reset(self):
        self.clear()
        for point in self.points:
            point.reset()

    def clear(self):
        for point in self.points:
            point.clear()
        self.dices.clear()

    def addPoint(self, point):
        self.points.append(point)

    def addDice(self, dice):
        # check if the detected dice is on the board
        if pointInPoly(dice.center, self.bbox):
            self.dices.append(dice)

    def addDisk(self, disk):
        # self.disks.append(disk)
        # Determine correct point to add
        for point in self.points:
            if pointInPoly(disk.center, point.bbox_warped):
                # TODO: dtermine color clustering
                point.addDisk(disk)

    # def updateDicesBoardPosition(self):
    #     center_bar = self.getBar().center[0]
    #     for dice in self.dices:
    #         if dice.center[0] <= center_bar:
    #             dice.board_position = BoardPosition.LEFT
    #         else:
    #             dice.board_position = BoardPosition.RIGHT

    def getBar(self):
        return self.points[len(self.points) - 1]

    def __str__(self):
        res = ""
        res += "dices: "
        for dice in self.dices:
            res += str(dice) + " "
        res += "\n"
        for point in self.points:
            res += str(point) + "\n"
        return res

    def copy(self):
        board = Board()
        board.bbox = self.bbox.copy()
        for point in self.points:
            newPoint = point.copy()
            board.addPoint(newPoint)

        board.dices = self.dices.copy()
        return board
        # return copy.deepcopy(self)
