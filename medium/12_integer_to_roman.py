"""
Given an integer, convert it to a roman numeral.

Constraints:
 • 1 <= num <= 3999
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        assert 1 <= num <= 3999
        result = ''
        for position in range(0, 4):
            digit = num // 10 ** position % 10
            result = self._get_digit_repr(digit, position) + result
        return result

    @staticmethod
    def _get_digit_repr(digit: int, position: int) -> str:
        assert 0 <= digit <= 9
        s1 = {
            0: 'I',
            1: 'X',
            2: 'C',
            3: 'M',
        }[position]
        s5 = {
            0: 'V',
            1: 'L',
            2: 'D',
            3: '-',
        }[position]
        s10 = {
            0: 'X',
            1: 'C',
            2: 'M',
            3: '-',
        }[position]
        return {
            0: '',
            1: s1,
            2: s1 * 2,
            3: s1 * 3,
            4: s1 + s5,
            5: s5,
            6: s5 + s1,
            7: s5 + s1 * 2,
            8: s5 + s1 * 3,
            9: s1 + s10,
        }[digit]


def test():
    solution = Solution()
    for test_case in (
         (3, 'III'),
         (58, 'LVIII'),
         (1994, 'MCMXCIV'),
         (1476, 'MCDLXXVI'),
    ):
        result = solution.intToRoman(test_case[0])
        assert result == test_case[1], result
    print("Test passed!")


test()
