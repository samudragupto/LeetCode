from typing import List
from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        patterns = defaultdict(list)
        for word in [beginWord] + wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                patterns[pattern].append(word)
        prev = defaultdict(list)
        queue = deque([beginWord])
        visited = set([beginWord])
        found = False

        while queue and not found:
            level_size = len(queue)
            level_visited = set()
            for _ in range(level_size):
                word = queue.popleft()
                if word == endWord:
                    found = True
                    break
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neighbor in patterns[pattern]:
                        if neighbor not in visited:
                            prev[neighbor].append(word)
                            if neighbor not in level_visited:
                                level_visited.add(neighbor)
                                queue.append(neighbor)
            visited.update(level_visited)

        if not found:
            return []
        def dfs(word):
            if word == beginWord:
                return [[beginWord]]
            res = []
            for p in prev[word]:
                for path in dfs(p):
                    res.append(path + [word])
            return res

        return dfs(endWord)
