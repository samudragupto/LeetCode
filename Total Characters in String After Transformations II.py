class Solution:
    MOD = 10**9 + 7

    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        def matrix_multiply(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % self.MOD
            return C

        def matrix_power(matrix, power):
            n = len(matrix)
            result = [[0] * n for _ in range(n)]
            for i in range(n):
                result[i][i] = 1
            
            base = [row[:] for row in matrix] 
            
            while power > 0:
                if power % 2 == 1:
                    result = matrix_multiply(result, base)
                base = matrix_multiply(base, base)
                power //= 2
            return result

        trans = [[0] * 26 for _ in range(26)]
        
        for c in range(26):
            count = nums[c]
            for i in range(count):
                next_char = (c + 1 + i) % 26
                trans[c][next_char] = 1

        final_trans = matrix_power(trans, t)

        initial_freq = [0] * 26
        for ch in s:
            initial_freq[ord(ch) - ord('a')] += 1

        final_freq = [0] * 26
        for i in range(26):
            for j in range(26):
                final_freq[j] = (final_freq[j] + initial_freq[i] * final_trans[i][j]) % self.MOD

        return sum(final_freq) % self.MOD
