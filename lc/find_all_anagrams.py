# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/

#Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

def findAnagrams(self, s: str, p: str) -> List[int]:
    max_value = 256  # total ascii characters
    output = []
    pattern_length = len(p)
    str_length = len(s)
    if pattern_length > str_length:
        return output
    count_pattern = [0] * max_value
    count_str = [0] * max_value

    for i in range(pattern_length):
        count_pattern[ord(p[i])] += 1
        count_str[ord(s[i])] += 1
    for i in range(pattern_length, str_length):
        result = self.match(count_pattern, count_str)
        if result:
            output.append(i - pattern_length)
        count_str[ord(s[i])] += 1
        count_str[ord(s[i - pattern_length])] -= 1
    result = self.match(count_pattern, count_str)
    if result:
        output.append(str_length - pattern_length)
    return output


def match(self, pat, s):
    for i in range(256):
        if pat[i] != s[i]:
            return False
    return True

# looks like the complexity is O(mn) but since the match is done for 256 chars so complexity becomes n* 256 => O(n)
