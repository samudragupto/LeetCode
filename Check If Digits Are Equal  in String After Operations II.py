class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        if n == 2:
            return s[0] == s[1]
        l = n - 2

        def get_digits(num, p):
            if num == 0:
                return [0]
            digits = []
            while num > 0:
                digits.append(num % p)
                num //= p
            return digits

        def binom_small(a, b, p):
            if b < 0 or b > a:
                return 0
            b = min(b, a - b)
            res = 1
            for i in range(1, b + 1):
                res = (res * (a - i + 1)) % p
                inv_i = pow(i, p - 2, p)
                res = (res * inv_i) % p
            return res

        def compute_sum(l, start, p):
            total = 0
            if p == 2:
                for k in range(l + 1):
                    if start + k >= n:
                        continue
                    sk = int(s[start + k]) % 2
                    if (k & l) == k:
                        total = (total + sk) % 2
            else:
                n_digits = get_digits(l, 5)
                d = len(n_digits)
                for k in range(l + 1):
                    if start + k >= n:
                        continue
                    sk = int(s[start + k]) % 5
                    k_digits = get_digits(k, 5)
                    k_digits += [0] * (d - len(k_digits))
                    luc = 1
                    valid = True
                    for nd, kd in zip(n_digits, k_digits):
                        if kd > nd:
                            valid = False
                            break
                        luc = (luc * binom_small(nd, kd, 5)) % 5
                    if valid:
                        total = (total + (luc * sk) % 5) % 5
            return total

        final0_mod2 = compute_sum(l, 0, 2)
        final0_mod5 = compute_sum(l, 0, 5)
        final1_mod2 = compute_sum(l, 1, 2)
        final1_mod5 = compute_sum(l, 1, 5)

        def get_mod10(mod2, mod5):
            for x in range(10):
                if x % 2 == mod2 and x % 5 == mod5:
                    return x
            return 0

        final0 = get_mod10(final0_mod2, final0_mod5)
        final1 = get_mod10(final1_mod2, final1_mod5)

        return final0 == final1
