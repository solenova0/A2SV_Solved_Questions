class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x: int) -> int:
            digits = list(map(int, str(x)))

            if len(digits) < 3:
                return 0

            cnt = 0
            for i in range(1, len(digits) - 1):
                if ((digits[i] > digits[i - 1] and digits[i] > digits[i + 1]) or
                    (digits[i] < digits[i - 1] and digits[i] < digits[i + 1])):
                    cnt += 1

            return cnt

        return sum(waviness(x) for x in range(num1, num2 + 1))