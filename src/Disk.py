from Color import Color


class Disk:
    def __init__(
        self,
        center=(0, 0),
        confidence=0,
        color=Color.WHITE,
    ):
        self.color = color
        self.confidence = confidence
        self.center = center

    def __str__(self):
        res = ""
        res += "w " if (self.color == Color.WHITE) else "b "
        return res

    def copy(self):
        disk = Disk(self.center, self.confidence, self.color)
        return disk
