from typing import List
from sortedcontainers import SortedList

class Solution:
    def minimumPairRemoval(self, A: List[int]) -> int:
        N = len(A)

        L = list(range(-1, N - 1))
        R = list(range(1, N + 1))

        self.inversions = sum(A[i] > A[i + 1] for i in range(N - 1))
        

        S = SortedList([ (A[i] + A[i + 1], i) for i in range(N - 1) ])

        def add(i):
            j = R[i]
            if 0 <= i < j < N:
                S.add((A[i] + A[j], i))
                self.inversions += A[i] > A[j]

        def remove(i):
            j = R[i]
            if 0 <= i < j < N:
                S.discard((A[i] + A[j], i))
                self.inversions -= A[i] > A[j]

        ans = 0
        while self.inversions:
            ans += 1
            s, i = S.pop(0) 
            j = R[i]
            h, k = L[i], R[j]

            remove(h)
            remove(i)
            remove(j)


            A[i] += A[j]
            R[i] = k
            if k < N:
                L[k] = i

            add(h)
            add(i)

        return ans
