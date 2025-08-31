class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if n1 == 0:
            return 0
        
        indexr = dict()
        s2_count = 0
        index = 0
        
        i = 0
        while i < n1:
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2_count += 1
                        index = 0
            
            if index in indexr:
                i_prev, s2_count_prev = indexr[index]
                interval = i - i_prev
                if interval == 0:
                    break
                repeat = (n1 - 1 - i) // interval
                s2_count += repeat * (s2_count - s2_count_prev)
                i += repeat * interval
            else:
                indexr[index] = (i, s2_count)
            i += 1
        
        return s2_count // n2
