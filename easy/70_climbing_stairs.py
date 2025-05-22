"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

5:
1 + 4
2 + 3

4:
1 + 3
2 + 2

3:
1 + 2
2 + 1
"""

class Solution:
    cache: dict = {}

    def climbStairs(self, n: int) -> int:
        """
        Use dynamic programming
        """
        return self._getComboCount(rest=n)

    def _getComboCount(self, rest: int) -> int:
        if rest in self.cache:
            return self.cache[rest]
        elif rest == 1:
            return 1
        elif rest == 2:
            return 2
        else:
            result = self._getComboCount(rest - 1) + self._getComboCount(rest - 2)
            self.cache[rest] = result
            return result


def test():
    solution = Solution()
    for i, (n, expected) in enumerate((
            (2, 2),
            (3, 3),
            (5, 8),
            (10, 89),
            (44, 1134903170),
    )):
        actual = solution.climbStairs(n)
        assert actual == expected, f"case {i}: n={n}: expected {expected}, got {actual}"
    print("Test passed!")


test()
