from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        We know a board is valid if
        for line x=[x , 0 <= x < 9] no point (x, y) where x = x and y=[0-9] is repeated
        for line y=[y, 0 <= y < 9] no point (x, y) where y = y and x=[0-9] is repeated
        for cubes 1 - 9 no cube has repeated items
        cube n: no point (x,y) in y = [0-2] and x = [x * n mod 4 - 1, - x * n mod 4] no point is repeated
        """
        # Check vertical lines
        # For vertical lines values for x will range from 0 - 8
        for x in range(0, 9, 1):
            # Use a dict for each new line
            found_numbers = defaultdict(bool)
            # For each x y will vary from 0 - 8
            for y in range(0, 9, 1):
                cell = board[y][x]
                if cell != ".":
                    if found_numbers[cell] == False:
                        found_numbers[cell] = True
                    else:
                        return False

        # Check horizontal lines
        # For each horizontal y will be a value from 0 - 8
        for y in range(0, 9, 1):
            # Use a dict for each line
            found_numbers = defaultdict(bool)
            # For each y x will vary from 0 - 8
            for x in range(0, 9, 1):
                cell = board[y][x]
                if cell != ".":
                    if found_numbers[cell] == False:
                        found_numbers[cell] = True
                    else:
                        return False
        

        # Check cubes
        x_low = 0
        x_high = 0
        y_low = 0
        y_high = 0
        # There are 9 cubes in total [1 - 9]
        for n in range(1, 10, 1):
            found_numbers = defaultdict(bool)

            if 1 <= n <= 3:
                y_low = 0
                y_high = 3
            elif 4 <= n <= 6:
                y_low = 3
                y_high = 6
            else:
                y_low = 6
                y_high = 9

            if n in [1,4,7]:
                x_low = 0
                x_high = 3
            elif n in [2,5,8]:
                x_low = 3
                x_high = 6
            else:
                x_low = 6
                x_high = 9

            # Cubes in y and x ranges must not have repeated numbers
            for x in range(x_low, x_high, 1):
                for y in range(y_low, y_high, 1):
                    cell = board[y][x]
                    if cell != ".":
                        if found_numbers[cell] == False:
                            found_numbers[cell] = True
                        else:
                            return False
                
        # return true
        return True
        