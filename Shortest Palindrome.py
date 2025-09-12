class Solution:
    def shortestPalindrome(self, s: str) -> str:
        temp = s + '#' + s[::-1]
        n = len(temp)
        lps = [0] * n
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j
        to_add = s[lps[-1]:][::-1]
        return to_add + s
