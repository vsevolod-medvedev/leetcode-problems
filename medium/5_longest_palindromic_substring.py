"""
Given a string s, return the longest palindromic substring in s.

Constraints:
 • 1 <= s.length <= 1000
 • s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        assert 1 <= length <= 1000, "Input string length is out of range"
        assert s.isalnum(), "Input string is not alpha-numeric"

        best = s[0]

        # Odd palindroms
        for i in range(1, length - 1):
            count = 1
            k = min(i, length - 1 - i)
            j = 1
            while j <= k and s[i - j] == s[i + j]:
                count += 2
                j += 1
            if count > len(best):
                best = s[i - count // 2: i + count // 2 + 1]

        # Even palindroms
        for i in range(1, length):
            count = 0
            k = min(i, length - i)
            j = 1
            while j <= k and s[i - j] == s[i - 1 + j]:
                count += 2
                j += 1
            if count > len(best):
                best = s[i - count // 2: i + count // 2]

        return best


def test():
    solution = Solution()
    for i, test_case in enumerate((
            ("babad", "bab"),
            ("cbbd", "bb"),
            ("ababcba", "abcba"),
            ("aba2222", "2222"),
            ("bb", "bb"),
    )):
        actual = solution.longestPalindrome(s=test_case[0])
        expected = test_case[1]
        assert actual == expected, f"case {i}: expected {expected}, got {actual}"
    print("Test passed!")


test()
