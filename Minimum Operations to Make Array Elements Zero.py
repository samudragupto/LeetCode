from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def count_operations(l: int, r: int) -> int:
            total_steps = 0
            power = 1 
            level = 0
            while power <= r:
                left = max(l, power)
                next_power = power * 4
                right = min(r, next_power - 1)
                if left <= right:
                    count = right - left + 1
                    total_steps += count * (level + 1)
                power = next_power
                level += 1
            return (total_steps + 1) // 2
        
        result = 0
        for l, r in queries:
            result += count_operations(l, r)
        return result
