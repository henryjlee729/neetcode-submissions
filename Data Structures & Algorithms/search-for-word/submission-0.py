class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(0, rows):
            for col in range(0, cols):
                if self.search(row, col, 0, board, word):
                    return True

        return False

    def search(self, row, col, index, board, word):
        if index == len(word):
            return True
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
            return False
        if board[row][col] != word[index]:
            return False
        if board[row][col] == '#':
            return False

        original = board[row][col]
        board[row][col] = '#'
        found = (self.search(row + 1, col, index + 1, board, word) or
            self.search(row - 1, col, index + 1, board, word) or
            self.search(row, col + 1, index + 1, board, word) or
            self.search(row, col - 1, index + 1, board, word))

        board[row][col] = original
        return found