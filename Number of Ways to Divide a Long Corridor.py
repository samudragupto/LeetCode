class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        seat_positions = [i for i, c in enumerate(corridor) if c == 'S']
        total_seats = len(seat_positions)
        if total_seats == 0 or total_seats % 2 != 0:
            return 0
        ways = 1
        for i in range(1, total_seats // 2):
            left = seat_positions[2 * i - 1]
            right = seat_positions[2 * i]
            ways = (ways * (right - left)) % mod
        return ways
