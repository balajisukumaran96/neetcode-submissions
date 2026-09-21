from abc import ABC, abstractmethod
from typing import List

class Validator(ABC):

    def __init__(self, current_set: List[set], board: List[List[str]]):
        self.current_set = current_set
        self.board = board

    @abstractmethod
    def isValid(self) -> bool:
        ...

class RowValidator(Validator):

    def isValid(self) -> bool:
        for row in range(9):
            for col in range(9):
                val = self.board[row][col]
                if val == ".":
                    continue
                if val in self.current_set[row]:
                    return False
                self.current_set[row].add(val)
        return True


class ColValidator(Validator):

    def isValid(self) -> bool:
        for row in range(9):
            for col in range(9):
                val = self.board[row][col]
                if val == ".":
                    continue
                if val in self.current_set[col]:
                    return False
                self.current_set[col].add(val)
        return True


class BoxValidator(Validator):

    def isValid(self) -> bool:
        for row in range(9):
            for col in range(9):
                val = self.board[row][col]
                if val == ".":
                    continue
                # Map 2D cell coordinates to 0-8 box index
                box_idx = (row // 3) * 3 + (col // 3)
                if val in self.current_set[box_idx]:
                    return False
                self.current_set[box_idx].add(val)
        return True


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validators = [
            RowValidator([set() for _ in range(9)], board),
            ColValidator([set() for _ in range(9)], board),
            BoxValidator([set() for _ in range(9)], board),
        ]

        for validator in validators:
            if not validator.isValid():
                return False

        return True