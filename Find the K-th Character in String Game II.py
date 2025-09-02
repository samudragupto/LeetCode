class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        lengths = [1]
        for op in operations:
            lengths.append(lengths[-1] * 2)

        def get_char(k, i):
            if i == 0:
                return 'a'
            half = lengths[i - 1]
            op = operations[i - 1]
            if k <= half:
                return get_char(k, i - 1)
            else:
                k -= half
                if op == 0:
                    return get_char(k, i - 1)
                else:
                    c = get_char(k, i - 1)
                    return chr(((ord(c) - ord('a') + 1) % 26) + ord('a'))
        return get_char(k, len(operations))
