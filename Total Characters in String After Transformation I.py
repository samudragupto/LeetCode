class Solution:
    MOD = 10**9 + 7

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        prev = [1] * 26  

        for _ in range(t):
            curr = [0] * 26
            for c in range(25):
                curr[c] = prev[c + 1] % self.MOD

            curr[25] = (prev[0] + prev[1]) % self.MOD

            prev = curr

        result = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            result = (result + prev[idx]) % self.MOD

        return result
