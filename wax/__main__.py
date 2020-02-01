from wax.converter import GameConverter
import sys


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    converter = GameConverter(input_path)
    game = converter.read_pgn()


if __name__ == '__main__':
    main()
