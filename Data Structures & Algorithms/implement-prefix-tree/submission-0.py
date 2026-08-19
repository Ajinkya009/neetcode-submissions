class TrieNode:
    __slots__ = ("children","is_end")

    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch)-ord("a")
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self._walk(prefix)
        return node is not None
    
    def _walk(self,word):
        node = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            if node.children[idx] is not None:
                node = node.children[idx]
            else:
                return None
        return node
        