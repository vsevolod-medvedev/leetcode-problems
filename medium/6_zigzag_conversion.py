"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:
 • 1 <= s.length <= 1000
 • s consists of English letters (lower-case and upper-case), ',' and '.'.
 • 1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        step = max(1, numRows * 2 - 2)
        result = ''
        for i in range(numRows):
            bias = step - i * 2
            for j in range(i, len(s), step):
                result += s[j]
                if bias != step and bias != 0 and j + bias < len(s):
                    result += s[j + bias]
        return result

def test():
    solution = Solution()
    for i, (source, num_rows, expected) in enumerate((
            # 1     7     D
            # 2   6 8   C E
            # 3 5   9 B
            # 4     A
            ("123456789ABCDE", 4, "17D268CE359B4A"),
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("A", 1, "A"),
    )):
        actual = solution.convert(source, num_rows)
        assert actual == expected, f"case {i}: {source}: expected {expected}, got {actual}"
    print("Test passed!")


test()
