from bitarray import bitarray


class GameState:
    NEW_GAME = {
        "white pawns": bitarray("0000000011111111000000000000000000000000000000000000000000000000"),
        "white knights": bitarray("0100001000000000000000000000000000000000000000000000000000000000"),
        "white bishops": bitarray("0010010000000000000000000000000000000000000000000000000000000000"),
        "white rooks": bitarray("1000000100000000000000000000000000000000000000000000000000000000"),
        "white queens": bitarray("0001000000000000000000000000000000000000000000000000000000000000"),
        "white king": bitarray("0000100000000000000000000000000000000000000000000000000000000000"),
        "black pawns": bitarray("0000000000000000000000000000000000000000000000001111111100000000"),
        "black knights": bitarray("0000000000000000000000000000000000000000000000000000000001000010"),
        "black bishops": bitarray("0000000000000000000000000000000000000000000000000000000000100100"),
        "black rooks": bitarray("0000000000000000000000000000000000000000000000000000000010000001"),
        "black queens": bitarray("0000000000000000000000000000000000000000000000000000000000010000"),
        "black king": bitarray("0000000000000000000000000000000000000000000000000000000000001000")
    }

    def __init__(self):
        self.bitboards = self.NEW_GAME

    def __str__(self):
        board_str = ""
        rank_str = "\n"
        for i in range(64):
            rank_str += self.get_piece(i)
            if i % 8 == 7:
                board_str = rank_str + board_str
                rank_str = "\n"
        return board_str

    def get_piece(self, square):
        if self.bitboards["white pawns"][square]:
            return "P"
        if self.bitboards["white knights"][square]:
            return "N"
        if self.bitboards["white bishops"][square]:
            return "B"
        if self.bitboards["white rooks"][square]:
            return "R"
        if self.bitboards["white queens"][square]:
            return "Q"
        if self.bitboards["white king"][square]:
            return "K"
        if self.bitboards["black pawns"][square]:
            return "p"
        if self.bitboards["black knights"][square]:
            return "n"
        if self.bitboards["black bishops"][square]:
            return "b"
        if self.bitboards["black rooks"][square]:
            return "r"
        if self.bitboards["black queens"][square]:
            return "q"
        if self.bitboards["black king"][square]:
            return "k"
        return "."
