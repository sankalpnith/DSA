# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


from collections import defaultdict


def groupAnagrams(strs):
    test_dict = defaultdict(list)
    for data in strs:
        key = tuple(sorted(data))
        test_dict[key].append(data)

    print(list(test_dict.values()))



strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)