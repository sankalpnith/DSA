#Given a string s, return the longest palindromic substring in s.
#Input: s = "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

def longestPalindrome(s: str) -> str:
    lon_pal = ''
    result = set()
    for i in range(len(s)):
        # odd number of characters in palindrome line abcba
        palindrome_with_common_mid = expand_around_center(s, i, i, result)
        # even number of characters in palindrome line abba
        palindrome_with_inbetween_mid = expand_around_center(s, i, i + 1, result)
        lon_pal = max(palindrome_with_common_mid, palindrome_with_inbetween_mid, lon_pal, key=len)
    print(lon_pal)
    print(result)
    return lon_pal

def expand_around_center(s, left, right, result):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        result.add(s[left: right+1])
        left -= 1
        right += 1
    return s[left + 1:right]

longestPalindrome("abaaa")
