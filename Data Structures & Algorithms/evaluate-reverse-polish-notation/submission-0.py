from abc import ABC, abstractmethod
from typing import List


class Solution:

    class ArithmeticOperation(ABC):
        @abstractmethod
        def apply(self, a: int, b: int) -> int:
            ...

    class Addition(ArithmeticOperation):
        def apply(self, a: int, b: int) -> int:
            return b + a

    class Subtraction(ArithmeticOperation):
        def apply(self, a: int, b: int) -> int:
            return b - a

    class Multiplication(ArithmeticOperation):
        def apply(self, a: int, b: int) -> int:
            return b * a

    class Division(ArithmeticOperation):
        def apply(self, a: int, b: int) -> int:
            return int(b / a)   # truncate toward zero, not floor

    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': Solution.Addition(),
            '-': Solution.Subtraction(),
            '*': Solution.Multiplication(),
            '/': Solution.Division(),
        }
        stack = []

        for token in tokens:
            if token in ops:
                a = stack.pop()      # right operand
                b = stack.pop()      # left operand
                stack.append(ops[token].apply(a, b))
            else:
                stack.append(int(token))

        return stack.pop()