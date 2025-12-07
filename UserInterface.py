import numpy as np
from numpy.ma.core import bitwise_or

from board import Board


class CommandLineUserInterface():

    def __init__(self):
        self.mines_array = np.zeros((4,4))
        self.board_size: int = 1

    def ask_board_size(self):
        self.board_width_size = int(input("Enter width board size: "))
        self.board_height_size = int(input("Enter height board size: "))
        return self.board_width_size, self.board_height_size

    def hello(self):
        print("Hello, World.")


    def draw_board(self, board:Board):

        wall = "|"
        title_line = ""
        second_line = ""
        numbers_line = "      "

        for x in range(board.height):
            numbers_line += str(x + 1) + "     "

        first_line = "   " + board.height * "| ̶̶ ̶ ̶ ̶̶ ̶̶" + "|"
        floor_line = "   " + board.height * "| ̶̶ ̶ ̶ ̶̶ ̶̶" + "|"
        first_line_length = len(first_line)
        #print ("board height= ", board.height, " - board with = ", board.width)
        title = "Mine Sweeper"
        title_position = round((first_line_length-len(title))/5)
        title_line = title_position * " " + title
        print(title_line)
        print(numbers_line)
        #print(top_line)

        print(first_line)
        for i in range (board.width):
            for j in range (board.height):
                if j == 0:
                    second_line += str(i + 1) + "  "
                second_line += wall + "  " + str(round(board.return_values(j, i))) + "  "

            print(second_line + wall)
            print(floor_line)
            second_line = ""


    def ask_for_mine_pos(self):
        pass


