class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        valid = False
        temp = []

        for line in source:
            i = 0
            if not valid:
                temp = []

            while i < len(line):
                if not valid and i+1 < len(line) and line[i:i+2] == "/*":
                    valid = True
                    i += 2
                elif valid and i+1 < len(line) and line[i:i+2] == "*/":
                    valid = False
                    i += 2
                elif not valid and i+1 < len(line) and line[i:i+2] == "//":
                    break
                elif not valid:
                    temp.append(line[i])
                    i += 1
                else:
                    i += 1

            if not valid and temp:
                res.append("".join(temp))

        return res