"""
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Constraints:
 • 0 <= s.length <= 3 * 104
 • s[i] is '(', or ')'.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Contains start indices of sequences
        max_len = 0
        for i, a in enumerate(s):
            if a == '(':
                stack.append(i)
            elif a == ')':
                if len(stack) == 1:
                    stack[0] = i
                else:
                    stack.pop()
                    max_len = max(max_len, i - stack[-1])
        return max_len


def test():
    solution = Solution()
    for i, test_case in enumerate((
            ("(()", 2),
            (")()())", 4),
            (")))(((", 0),
            ("()(()", 2),
    )):
        actual = solution.longestValidParentheses(s=test_case[0])
        expected = test_case[1]
        assert actual == expected, f"Case {i}, {test_case[0]}: expected {expected}, got {actual}"
    print("Test passed!")


test()
