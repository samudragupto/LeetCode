from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count
        if len(s) < total_length:
            return []
        
        from collections import Counter
        words_map = Counter(words)
        
        res = []
        
        for offset in range(word_length):
            left = offset
            count = 0
            seen = Counter()
            
            for j in range(offset, len(s) - word_length + 1, word_length):
                word = s[j:j + word_length]
                if word in words_map:
                    seen[word] += 1
                    count += 1
                    
                    while seen[word] > words_map[word]:
                        left_word = s[left:left + word_length]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_length
                    
                    if count == word_count:
                        res.append(left)
                        left_word = s[left:left + word_length]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_length
                else:
                    seen.clear()
                    count = 0
                    left = j + word_length
        
        return res
