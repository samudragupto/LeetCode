class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def to_base_k(num: int, base: int) -> str:
            if num == 0:
                return '0'
            digits = []
            while num > 0:
                digits.append(str(num % base))
                num //= base
            return ''.join(reversed(digits))

        res = []
        length = 1

        def generate_palindromes(length: int):
            half = (length + 1) // 2
            start = 10**(half - 1) if half > 1 else 1
            end = 10**half
            for num in range(start, end):
                s = str(num)
                if length % 2 == 0:
                    palindrome = int(s + s[::-1])
                else:
                    palindrome = int(s + s[-2::-1])
                yield palindrome

        while len(res) < n:
            for palindrome in generate_palindromes(length):
                s_base_k = to_base_k(palindrome, k)
                if is_palindrome(s_base_k):
                    res.append(palindrome)
                    if len(res) == n:
                        break
            length += 1
        return sum(res)
