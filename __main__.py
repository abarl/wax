from gamestate import GameState
import sys

def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    read_pgn(input_path)


def read_pgn(pgn_path):
    with open(pgn_path) as in_file:
        meta_data = read_meta_data(in_file)
        game = read_game(in_file)


def read_game(in_file):
    game = []
    game_state = GameState()

    moves = filter(lambda x: '.' not in x and '-' not in x, in_file.readline().split(' '))
    print(moves)


def read_meta_data(in_file):
    line = in_file.readline()
    meta_data = {}

    while line[0] == '[':
        parts = line.split('"')
        meta_data[parts[0].replace(' ','').replace('[','')] = parts[1]
        line = in_file.readline()

    return meta_data


if __name__ == '__main__':
    main()
