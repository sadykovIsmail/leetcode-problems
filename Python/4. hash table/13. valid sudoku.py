from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unique_raw = dict()
        unique_quarter1 = {1: set(), 2: set(), 3: set()}
        unique_quarter2 = {1: set(), 2: set(), 3: set()}
        unique_quarter3 = {1: set(), 2: set(), 3: set()}
        for i_col, column in enumerate(board):
            unique = set()



            for i_it, item in enumerate(column):
                if item != '.':
                    #check for each column unique
                    if item in unique:
                        return False
                    elif item not in unique:
                        unique.add(item)
                    #check for each row unique
                    if i_it in unique_raw.keys():
                        if item in unique_raw[i_it]:
                            return False
                        else:
                            unique_raw[i_it].add(item)
                    elif i_it not in unique_raw.keys():
                        unique_raw[i_it] = set(item)

                    #check for each quarted unique
                    if i_col <= 2:
                        if i_it <= 2:
                            if item in unique_quarter1[1]:
                                return False
                            else:
                                unique_quarter1[1].add(item)
                        elif i_it <= 5:
                            if item in unique_quarter1[2]:
                                return False
                            else:
                                unique_quarter1[2].add(item)
                        elif i_it <= 8:
                            if item in unique_quarter1[3]:
                                return False
                            else:
                                unique_quarter1[3].add(item)

                    elif i_col <= 5:
                        if i_it <= 2:
                            if item in unique_quarter2[1]:
                                return False
                            else:
                                unique_quarter2[1].add(item)
                        elif i_it <= 5:
                            if item in unique_quarter2[2]:
                                return False
                            else:
                                unique_quarter2[2].add(item)
                        elif i_it <= 8:
                            if item in unique_quarter2[3]:
                                return False
                            else:
                                unique_quarter2[3].add(item)

                    elif i_col <= 8:
                        if i_it <= 2:
                            if item in unique_quarter3[1]:
                                return False
                            else:
                                unique_quarter3[1].add(item)
                        elif i_it <= 5:
                            if item in unique_quarter3[2]:
                                return False
                            else:
                                unique_quarter3[2].add(item)
                        elif i_it <= 8:
                            if item in unique_quarter3[3]:
                                return False
                            else:
                                unique_quarter3[3].add(item)







        print(unique_raw)
        return True


exa = Solution()
test = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
print(exa.isValidSudoku(test))


"""What is actually needed

class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                box = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True

"""

"""The fastest version

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use integers as bitmasks to track seen numbers
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                # Convert char to number and create bitmask
                num = int(val) - 1  # 0-8 instead of 1-9
                bit = 1 << num

                # Calculate box index
                box_idx = (r // 3) * 3 + (c // 3)

                # Check if number already exists using bitwise AND
                if rows[r] & bit or cols[c] & bit or boxes[box_idx] & bit:
                    return False

                # Mark number as seen using bitwise OR
                rows[r] |= bit
                cols[c] |= bit
                boxes[box_idx] |= bit

        return True
"""
