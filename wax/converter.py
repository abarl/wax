from game import WaxGame
from gamestate import GameState


class GameConverter:
    def __init__(self, input_path):
        self.in_file = open(input_path)

    def __pgn_to_wax(self, moves):
        game = WaxGame()
        return game

    def __read_meta_data(self):
        line = self.in_file.readline()
        meta_data = {}

        while line[0] == '[':
            parts = line.split('"')
            meta_data[parts[0].replace(' ','').replace('[','').lower()] = parts[1]
            line = self.in_file.readline()

        return meta_data

    def __read_moves(self):
        moves = filter(lambda x: '.' not in x and '-' not in x, self.in_file.readline().split(' '))
        return moves

    def read_pgn(self):
        meta_data = self.__read_meta_data()
        moves = self.__read_moves()
        game = self.__pgn_to_wax(moves)
        game.add_meta_data(meta_data)
        return game
