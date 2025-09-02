class Solution:
    def numberOfPairs(self, points):
        n = len(points)
        count = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                Ax, Ay = points[i]
                Bx, By = points[j]
                if (Ax <= Bx and Ay >= By) and (Ax < Bx or Ay > By):
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if Ax <= x <= Bx and By <= y <= Ay:
                            valid = False
                            break
                    if valid:
                        count += 1

        return count
