from functions import Sudoku
import fire
import logging

logger = logging.getLogger(__name__)


class Main(object):

    @staticmethod
    def solve_sudoku():
        board = []
        size = list(map(int, input('Size of board (rows columns) separated by space: ').strip().split()))[0:2]
        for i in range(size[1]):
            while True:
                print('For empty values type "0"')
                line = list(map(int, input(f'Line {i + 1} (input values separated by a space): ').strip().split()))[
                       :size[0]]
                len_line = len(line)
                if len_line != size[0]:
                    print(f'\n\nInput of line {i+1} has length {len_line}, input must be of size {size[0]}!')
                    print('Try again!\n')
                    continue
                else:
                    break

            board.append(line)

        # Create sudoku object
        sudoku = Sudoku(board=board)

        # Print original sudoku
        print('\n\nUnsolved Sudoku:\n')
        sudoku.print_board()

        # Print solved sudoku
        print('\n\n- - - - - - - - - - - -\n\nSolved Sudoku:\n')
        sudoku.solve()
        sudoku.print_board()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    fire.Fire(Main)
