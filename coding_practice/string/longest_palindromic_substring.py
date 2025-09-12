"""
Find the longest palindromic substring.
"""


def longest_palindromic_substring(s):
    def expand_from_center(left: int, right: int) -> str:
        # Expand while in bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Slice between left+1 and right (because loop went one step too far)
        """
        For i = 0 , Odd length
        s[left+1:right] = s[-1+1 : 1] = s[0:1]
        """
        return s[left + 1: right]

    longest = ""

    for i in range(len(s)):
        # Odd-length palindrome
        palindrome1 = expand_from_center(i, i)
        # Even-length palindrome
        palindrome2 = expand_from_center(i, i + 1)

        # Update longest if needed
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest


print(longest_palindromic_substring("babad"))
