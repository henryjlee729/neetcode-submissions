class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.isEndOfWord = True
        current.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        rows = len(board)
        cols = len(board[0])
        for row in range(0, rows):
            for col in range(0, cols):
                self.dfs(row, col, trie.root, board, result)

        return list(result)

    def dfs(self, row, col, node, board, result):
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
            return
        if board[row][col] == '#':
            return

        c = board[row][col]
        if c not in node.children:
            return
        
        node = node.children[c]
        if node.isEndOfWord:
            result.add(node.word)

        original = c
        board[row][col] = '#'
        self.dfs(row + 1, col, node, board, result)
        self.dfs(row - 1, col, node, board, result)
        self.dfs(row, col + 1, node, board, result)
        self.dfs(row, col - 1, node, board, result)

        board[row][col] = original