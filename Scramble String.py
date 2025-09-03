from functools import lru_cache

class Solution:
    def isScramble(self, s1, s2):
        @lru_cache(maxsize=None)
        def helper(str1, str2):
            if str1 == str2:
                return True
            if sorted(str1) != sorted(str2):
                return False
            n = len(str1)
            for i in range(1, n):
                if helper(str1[:i], str2[:i]) and helper(str1[i:], str2[i:]):
                    return True
                if helper(str1[:i], str2[-i:]) and helper(str1[i:], str2[:-i]):
                    return True
            return False
        return helper(s1, s2)
