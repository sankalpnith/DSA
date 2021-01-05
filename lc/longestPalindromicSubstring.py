#Given a string s, return the longest palindromic substring in s.
#Input: s = "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lon_pal = ''
        for i in range(len(s)):
            # odd number of characters in palindrome line abcba
            palindrome_with_common_mid = self.expand_around_center(s, i, i)
            # even number of characters in palindrome line abba
            palindrome_with_inbetween_mid = self.expand_around_center(s, i, i + 1)
            lon_pal = max(palindrome_with_common_mid, palindrome_with_inbetween_mid, lon_pal, key=len)
        return lon_pal

    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]