class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = { ')':'(', '}':'{', ']':'['}

        for p in s:

            if p in mapping:

                if stack:
                    openp = stack.pop()
                else:
                    openp = '#'

                if mapping[p] != openp:
                    return False

            else:
                stack.append(p)

        return not stack


        