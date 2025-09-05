from typing import List

class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0
        for v in nums:
            total_xor ^= v
        def build_basis(arr: List[int]) -> List[int]:
            basis: List[int] = []
            for num in arr:
                for b in basis:
                    num = min(num, num ^ b)
                if num:
                    basis.append(num)
            return basis

        def max_subset_xor(basis: List[int]) -> int:
            best = 0
            for b in basis:
                best = max(best, best ^ b)
            return best

        best_total = 0
        for mask in range(1, 1 << n):
            and_B = -1 
            xor_B = 0       
            rest: List[int] = []  

            for i in range(n):
                if (mask >> i) & 1:   
                    xor_B ^= nums[i]
                    if and_B == -1:
                        and_B = nums[i]
                    else:
                        and_B &= nums[i]
                else:
                    rest.append(nums[i])

            xor_R = total_xor ^ xor_B  
            movable_mask = ~xor_R
            reduced = [x & movable_mask for x in rest]
            basis = build_basis(reduced)
            best_t = max_subset_xor(basis) 

            current = and_B + xor_R + (best_t << 1) 
            best_total = max(best_total, current)

        return best_total
