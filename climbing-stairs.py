# Recursion + Memoization Approach

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(n):
            if n == 0 or n == 1:
                return 1
            if n in cache:
                return cache[n]

            else:
                steps = helper(n - 1) + helper(n - 2)
                cache[n] = steps
                return cache[n]

        return helper(n)
