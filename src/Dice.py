from Color import Color
from BoardPosition import BoardPosition


class Dice:
    def __init__(
        self,
        id=0,
        center=(0, 0),
        confidence=0,
        board_position=BoardPosition.LEFT,
        color=Color.WHITE,
    ):
        self.id = id
        self.value = id + 1
        self.confidence = confidence
        self.board_position = board_position
        self.color = color
        self.center = center

    def __str__(self):
        res = str(self.value)
        # res += "w " if (self.color == Color.WHITE) else "b "
        return res

    def __repr__(self):
        return str(self.value)
