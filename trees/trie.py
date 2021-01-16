# https://leetcode.com/problems/implement-trie-prefix-tree/submissions/

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.word = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for char in word:
            if char not in node.data:
                node.data[char] = Trie()
            node = node.data[char]
        node.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for char in word:
            if not node.data.get(char):
                return False
            node = node.data.get(char)
        return True if node.word else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for char in prefix:
            if not node.data.get(char):
                return False
            node = node.data.get(char)
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)