from bitarray import bitarray


# noinspection SpellCheckingInspection
class GameState:
    NEW_GAME = {
        "white pawns": bitarray("0000000011111111000000000000000000000000000000000000000000000000"),
        "white knights": bitarray("0100001000000000000000000000000000000000000000000000000000000000"),
        "white bishops": bitarray("0010010000000000000000000000000000000000000000000000000000000000"),
        "white rooks": bitarray("1000000100000000000000000000000000000000000000000000000000000000"),
        "white queens": bitarray("0001000000000000000000000000000000000000000000000000000000000000"),
        "white king": bitarray("0000100000000000000000000000000000000000000000000000000000000000"),
        "black pawns": bitarray("0000000000000000000000000000000000000000000000000111111110000000"),
        "black knights": bitarray("0000000000000000000000000000000000000000000000000000000001000010"),
        "black bishops": bitarray("0000000000000000000000000000000000000000000000000000000000100100"),
        "black rooks": bitarray("0000000000000000000000000000000000000000000000000000000010000001"),
        "black queens": bitarray("0000000000000000000000000000000000000000000000000000000000010000"),
        "black king": bitarray("0000000000000000000000000000000000000000000000000000000000001000")
    }

    def __init__(self):
        self.bitboards = self.NEW_GAME
