# https://leetcode.com/problems/top-k-frequent-words/submissions/

# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest.
# If two words have the same frequency, then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.defaultdict(int)
        for word in words:
            counter[word] += 1
        order = sorted(counter, key=lambda x: (-counter[x],x))
        # first sorted by frequency (-)signifies decreasing as default is increasing, if same then sort by word(lexicographic ordering)
        return order[:k]

