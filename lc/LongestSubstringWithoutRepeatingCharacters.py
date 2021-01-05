def lengthOfLongestSubstring(self, s: str) -> int:
    start = 0
    # visited is a dictionary containing character and index of the character
    visited = dict()
    output = list()
    for i in range(len(s)):
        if s[i] in visited.keys():
            start = max(visited.get(s[i])+1, start)
        if len(output) < i - start + 1:
            output = s[start:i+1]
        visited[s[i]] = i
    return len(output)
