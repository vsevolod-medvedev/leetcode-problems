"""
Given a roman numeral, convert it to an integer.

Constraints:
 • 1 <= s.length <= 15
 • s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
 • It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        digit_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        pair_map = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        i = 0
        sum = 0
        while i < len(s):
            digit = s[i]
            next = s[i + 1] if i < len(s) - 1 else ''
            pair = digit + next
            if next and pair in pair_map.keys():
                sum += pair_map[pair]
                i += 2
            else:
                sum += digit_map[digit]
                i += 1
        return sum


def test():
    solution = Solution()
    assert solution.romanToInt('III') == 3
    assert solution.romanToInt('LVIII') == 58
    assert solution.romanToInt('MCMXCIV') == 1994
    assert solution.romanToInt('MCDLXXVI') == 1476
    print("Test passed!")


test()
