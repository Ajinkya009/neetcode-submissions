class TrieNode:
    __slots__ = ("children","is_end")
    
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch)-ord("a")
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index,node):
            if not node:
                return False
            for idx in range(index,len(word)):
                ind = ord(word[idx]) - ord("a")
                
                if word[idx]==".":
                    for child in node.children:
                        if dfs(idx+1,child):
                            return True
                    return False
                else:
                    if node and not node.children[ind]:
                        return False
                    node = node.children[ind]
            return node.is_end
        return dfs(0,self.root)

