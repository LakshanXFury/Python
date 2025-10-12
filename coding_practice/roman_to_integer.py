"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
"""


# def romanToInt(s: str) -> int:
#     roman_map = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50,
#         'C': 100, 'D': 500, 'M': 1000
#     }
#     total = 0
#     n = len(s)
#
#     for i in range(n):
#         current_value = roman_map[s[i]]
#         # print(current_value)
#
#         # check for subtraction cases
#         if i + 1 < n and roman_map[s[i + 1]] > current_value:
#             total -= current_value
#         else:
#             total += current_value
#     return total

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)

        for i in range(n):
            current_value = roman_map[s[i]]

            # check for subtraction cases
            if i + 1 < n and roman_map[s[i + 1]] > current_value:
                total -= current_value
            else:
                total += current_value

        return total


# When the if statement fails the current value add to the total, vice versa when it passes
# In this => roman_map[s[i + 1]] > current_value
# If i = 2, then [s[i + 1]] becomes [s[3]] => it will fetch the 4th value from the string as counting starts form 0

sol = Solution()  # Create an instance (an object) of the class

print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
