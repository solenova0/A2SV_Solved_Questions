class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        zeros = t.count("0")
        ones = len(t) - zeros

        result = []

        for char in s:
            if char == "1":
                if zeros > 0:
                    result.append("1")
                    zeros -= 1
                else:
                    result.append("0")
                    ones -= 1
            else:  # char == "0"
                if ones > 0:
                    result.append("1")
                    ones -= 1
                else:
                    result.append("0")
                    zeros -= 1

        return "".join(result)