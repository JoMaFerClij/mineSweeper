from UserInterface import CommandLineUserInterface
from asciiList import AsciiList
from board import Board


def main():
    user_interface = CommandLineUserInterface()
    board_size = user_interface.ask_board_size()
    board = Board(board_size[0], board_size[1])

    board.fill_mines_array()
    user_interface.draw_board(board)

    #user_interface.draw_board()


if __name__ == '__main__':
    main()