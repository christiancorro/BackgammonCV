from Board import Board


class Snapshot:
    def __init__(self, frame_index: int, board: Board, frame, overlay):
        self.id = 0
        self.frame_index = frame_index
        self.board = board
        self.frame = frame
        self.overlay = overlay

    def __str__(self) -> str:
        res = ""
        res += "Snapshot " + str(self.id)
        res += "\n    frame: " + str(self.frame_index)
        res += "\n    dices: " + str(self.board.dices)
        return res
