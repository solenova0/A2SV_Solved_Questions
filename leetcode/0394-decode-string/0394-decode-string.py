class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for v in s:
            if v is not "]":
                stack.append(v)
            else:
                temp = ""
                while stack[-1] is not "[":
                    temp = stack.pop() + temp
                stack.pop()

                mult = ""
                while stack and stack[-1].isdigit():
                    mult = stack.pop() + mult

                stack.append(int(mult) * temp)

        return "".join(stack)
