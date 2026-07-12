class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)
    
    def dfs(self, node, index, word):
        if index == len(word):
            return node.isEndOfWord

        c = word[index]
        if c != '.':
            if c not in node.children:
                return False

            return self.dfs(node.children[c], index + 1, word)
        else:
            for child in node.children.values():
                if self.dfs(child, index + 1, word):
                    return True
                
            return False