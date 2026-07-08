class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return False
        if len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False

        stack = []
        open_to_close = {"(": ")", "{": "}", "[": "]"}

        for bracket in s:
            if bracket in open_to_close:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if open_to_close[top] == bracket:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0