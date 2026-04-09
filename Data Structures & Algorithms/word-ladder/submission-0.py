from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        n = len(endWord)
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(n):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set(beginWord)

        while q:
            word, level = q.popleft()

            for i in range(n):
                pattern = word[:i] + '*' + word[i+1:]
                for nei in pattern_map[pattern]:
                    if nei == endWord:
                        return level + 1
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, level+1))
                
                pattern_map[pattern] = []
        
        return 0