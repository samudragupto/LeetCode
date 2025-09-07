from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10**9 + 7
        n = len(nums)
        if multiplier == 1:
            return [x % MOD for x in nums]
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        result = nums[:]
        max_val = max(nums)
        operations_done = 0
        while operations_done < k:
            val, idx = heap[0]
            if val >= max_val:
                break
            heapq.heappop(heap)
            new_val = val * multiplier
            result[idx] = new_val
            heapq.heappush(heap, (new_val, idx))
            operations_done += 1
        remaining_ops = k - operations_done
        if remaining_ops > 0:
            base_multiplier = pow(multiplier, remaining_ops // n, MOD)
            extra_ops = remaining_ops % n
            indexed_values = [(result[i], i) for i in range(n)]
            indexed_values.sort()
            for i in range(n):
                val, idx = indexed_values[i]
                result[idx] = (result[idx] * base_multiplier) % MOD
                if i < extra_ops:
                    result[idx] = (result[idx] * multiplier) % MOD
        return [x % MOD for x in result]
