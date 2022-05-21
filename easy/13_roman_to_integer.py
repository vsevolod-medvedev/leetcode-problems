class Solution:
    def romanToInt(self, s: str) -> int:
        digitMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        pairMap = {
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
            if next and pair in pairMap.keys():
                sum += pairMap[pair]
                i += 2
            else:
                sum += digitMap[digit]
                i += 1
        return sum


print(Solution().romanToInt('III'))
print(Solution().romanToInt('LVIII'))  # 58
print(Solution().romanToInt('MCMXCIV'))  # 1994
print(Solution().romanToInt('MCDLXXVI'))  # 1476
