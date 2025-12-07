from UserInterface import CommandLineUserInterface
from asciiList import AsciiList
from board import Board


def main():
    ascii_list = AsciiList
    #ascii_list.list_all()
    #print("¯¯¯---___")
    user_interface = CommandLineUserInterface()
    board_size = user_interface.ask_board_size()
    board = Board(board_size[0], board_size[1])

    board.fill_mines_array()
    user_interface.draw_board(board)
    x: int = 1
    y: int = 1
    #print("Value in " + str(x) + ", " + str(y) + " is: " + str(board.return_values(x, y)))


if __name__ == '__main__':
    main()