from typing import List
import bisect

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(k: int) -> bool:
            if k == 0:
                return True
            avail_workers = workers[-k:]
            avail_workers.sort()
            remain_pills = pills
            for t in range(k-1, -1, -1):
                task = tasks[t]
                idx = bisect.bisect_left(avail_workers, task)
                if idx < len(avail_workers):
                    del avail_workers[idx]
                else:
                    pill_req = task - strength
                    idx = bisect.bisect_left(avail_workers, pill_req)
                    if idx < len(avail_workers) and remain_pills > 0:
                        del avail_workers[idx]
                        remain_pills -= 1
                    else:
                        return False
            return True
        low, high = 0, min(len(tasks), len(workers))
        while low < high:
            mid = (low + high + 1) // 2
            if can_assign(mid):
                low = mid
            else:
                high = mid - 1
        return low
