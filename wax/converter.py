from gamestate import GameState


class GameConverter:


    def __init__(self, input_path):
        self.in_file = open(input_path)


    def read_pgn(self):
        meta_data = self.read_meta_data()
        game = self.read_game()


    def read_game(self):
        game = []
        game_state = GameState()

        moves = filter(lambda x: '.' not in x and '-' not in x, self.in_file.readline().split(' '))
        print(moves)


    def read_meta_data(self):
        line = self.in_file.readline()
        meta_data = {}

        while line[0] == '[':
            parts = line.split('"')
            meta_data[parts[0].replace(' ','').replace('[','')] = parts[1]
            line = self.in_file.readline()

        return meta_data


