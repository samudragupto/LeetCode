from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        result = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, node):
            if not (0 <= r < m and 0 <= c < n) or board[r][c] not in node.children:
                return
            ch = board[r][c]
            next_node = node.children[ch]
            if next_node.word:
                result.add(next_node.word)
                next_node.word = None  # Avoid duplicates
            board[r][c] = '#'
            for dr, dc in directions:
                dfs(r + dr, c + dc, next_node)
            board[r][c] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)

        return list(result)
