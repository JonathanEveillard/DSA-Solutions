class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Mapping = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c not in Mapping:
                stack.append(c)
                continue
            if not stack or stack[-1] != Mapping[c]:
                return False
            stack.pop()

        return not stack
