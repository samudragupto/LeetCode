class Solution:
    def fullJustify(self, words, maxWidth):
        res, curr, num_of_letters = [], [], 0
        
        for word in words:
            if num_of_letters + len(word) + len(curr) > maxWidth:
                if len(curr) == 1:
                    res.append(curr[0] + ' ' * (maxWidth - num_of_letters))
                else:
                    total_spaces = maxWidth - num_of_letters
                    spaces_between_words, extra = divmod(total_spaces, len(curr) - 1)
                    line = ''
                    for i in range(len(curr) - 1):
                        line += curr[i] + ' ' * (spaces_between_words + (1 if i < extra else 0))
                    line += curr[-1]
                    res.append(line)
                curr, num_of_letters = [], 0
            curr.append(word)
            num_of_letters += len(word)
        
        last_line = ' '.join(curr).ljust(maxWidth)
        res.append(last_line)
        
        return res
