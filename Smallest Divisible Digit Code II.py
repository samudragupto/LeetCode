class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def factorize(n):
            factors = [0] * 8
            for p in [2, 3, 5, 7]:
                while n % p == 0:
                    factors[p] += 1
                    n //= p
            return factors if n == 1 else None
        
        target = factorize(t)
        if target is None:
            return "-1"
        
        digit_primes = {
            2: [2], 3: [3], 4: [2, 2], 5: [5], 
            6: [2, 3], 7: [7], 8: [2, 2, 2], 9: [3, 3]
        }
        
        def build_digits(factors):
            f = factors[:]
            digits = []
            
            digits.extend([8] * (f[2] // 3))
            f[2] %= 3
            
            digits.extend([9] * (f[3] // 2))
            f[3] %= 2
            
            digits.extend([7] * f[7])
            digits.extend([5] * f[5])
            
            if f[2] > 0 and f[3] > 0:
                pairs = min(f[2], f[3])
                digits.extend([6] * pairs)
                f[2] -= pairs
                f[3] -= pairs
            
            if f[2] >= 2:
                digits.extend([4] * (f[2] // 2))
                f[2] %= 2
            
            digits.extend([3] * f[3])
            digits.extend([2] * f[2])
            
            return digits
        
        def get_factors(s):
            factors = [0] * 8
            for c in s:
                if c == '0':
                    return None
                d = int(c)
                if d in digit_primes:
                    for p in digit_primes[d]:
                        factors[p] += 1
            return factors
        
        def satisfies(factors):
            return factors and all(factors[i] >= target[i] for i in range(2, 8))
        
        if '0' not in num and satisfies(get_factors(num)):
            return num
        
        n = len(num)
        
        if '0' in num:
            for pos in range(n):
                if num[pos] == '0':
                    for digit in range(1, 10):
                        prefix = num[:pos] + str(digit)
                        remaining_positions = n - len(prefix)
                        
                        if remaining_positions == 0:
                            factors = get_factors(prefix)
                            if satisfies(factors):
                                return prefix
                        else:
                            prefix_factors = get_factors(prefix)
                            if not prefix_factors:
                                continue
                                
                            need = [0] * 8
                            for i in range(2, 8):
                                need[i] = max(0, target[i] - prefix_factors[i])
                            
                            if all(need[i] == 0 for i in range(2, 8)):
                                return prefix + '1' * remaining_positions
                            
                            required_digits = build_digits(need)
                            if len(required_digits) <= remaining_positions:
                                all_digits = required_digits + [1] * (remaining_positions - len(required_digits))
                                all_digits.sort()
                                suffix = ''.join(map(str, all_digits))
                                return prefix + suffix
        
        for pos in range(n - 1, -1, -1):
            for digit in range(int(num[pos]) + 1, 10):
                prefix = num[:pos] + str(digit)
                prefix_factors = get_factors(prefix)
                if not prefix_factors:
                    continue
                
                remaining_positions = n - len(prefix)
                
                need = [0] * 8
                for i in range(2, 8):
                    need[i] = max(0, target[i] - prefix_factors[i])
                
                if all(need[i] == 0 for i in range(2, 8)):
                    return prefix + '1' * remaining_positions
                
                required_digits = build_digits(need)
                if len(required_digits) <= remaining_positions:
                    all_digits = required_digits + [1] * (remaining_positions - len(required_digits))
                    all_digits.sort()
                    suffix = ''.join(map(str, all_digits))
                    return prefix + suffix
        
        required_digits = build_digits(target)
        all_digits = required_digits[:]
        all_digits.sort()
        result = ''.join(map(str, all_digits))
        
        while len(result) < len(num) or (len(result) == len(num) and result < num):
            result = '1' + result
        
        return result
