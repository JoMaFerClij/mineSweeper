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

    """
    for every row
        for every column
            if row == 0 
                print number
                print top part
            if column == 0
                print number
                print left side
            
            print middle side
            print left side
            
    """

    """def array_mine_data(self):
        self.randomines = 0
        print ("self.board_size  is type ", type(self.board_size), " and its value is = ", self.board_size)
        #array_mine = [[2,3,4,5], ["a", "b", "c", "d"], [6,7,8,9], [2, 4, 6, 8]]
        for i in range(self.board_size):
            for j in range(self.board_size):
                if random() < 0.33:
                    randomines = 1
                    self.mines_array[i, j] = randomines
                    print(self.mines_array)
                    self.randomines = 0

        #self.mines_array[1, 2] = 4
        #print("Now the array has a number 4: ", self.mines_array)
    """

    def draw_board(self, board:Board):

        wall = "|"
        floor = "_____"
        first_line = "  "
        second_line = ""
        numbers_line = "      "
        for x in range(board.height):
            numbers_line += str(x + 1) + "     "
        first_line = "   " + board.height * "| ̶̶ ̶ ̶ ̶̶ ̶̶" + "|"
        #top_line = board.height * "______" + "_"
        #first_line = (board.height * "|     ") + "|"
        floor_line = "   " + board.height * "| ̶̶ ̶ ̶ ̶̶ ̶̶" + "|"

        #print ("board height= ", board.height, " - board with = ", board.width)
        print ("  " + (round(board.height/1.6)  * "    "), "Mine Sweeper")
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


    def ask_for_cell(self):
        pass



        """  #board_size = self.ask_board_size()
            title_pos = "    " * int(board.width)
            column_number = "  "
            top_line = "     "
            draw_cells_first_line = ""
            draw_cells_second_line = ""
            draw_cells_floor = "     "
            draw_cells_wall_number = " "
    
            # Print title text
            print("\n", title_pos.removeprefix("  "), "MineSweeper\n")
    
            # Print column numbers
            for i in range(board.width):
                column_number = column_number + "       " + str(i+1)
            print(column_number)
    
            # Top line
            for i in range(board.width):
                top_line = top_line + "________"
            print(top_line)
    
            # Cells
            # First line
            for i in range(board.width):
                draw_cells_first_line += "|       "
            draw_cells_first_line = "     " + draw_cells_first_line
    
            # Second line
            for i in range(board.width):
                #letter = chr(65 + (int(random() * 26)))
                letter = "M"
                draw_cells_second_line += "|" + "   " + letter + "   "
            draw_cells_second_line = "     " + draw_cells_second_line
    
    
            for i in range(board.width):
                draw_cells_floor += "|_______"
    
    
            for i in range(board.width):
                draw_cells_wall_number = str(i+1) + draw_cells_second_line.removeprefix(" ") + "|"
    
                print(draw_cells_first_line + "|")
                print(draw_cells_wall_number)
    
                print(draw_cells_floor + "|")
    
    """
