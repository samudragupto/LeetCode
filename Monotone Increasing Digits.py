class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(map(int, str(n)))
        i = 1
        while i < len(digits) and digits[i] >= digits[i - 1]:
            i += 1
        if i < len(digits):
            while i > 0 and digits[i] < digits[i - 1]:
                digits[i - 1] -= 1
                i -= 1
            for j in range(i + 1, len(digits)):
                digits[j] = 9
        return int("".join(map(str, digits)))
