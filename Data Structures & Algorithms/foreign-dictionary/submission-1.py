from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ''
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        topo = ''
        q = deque([c for c in indegree if indegree[c] == 0])

        while q:
            w = q.popleft()
            topo += w

            for nei in graph[w]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            
        if len(topo) != len(indegree):
            return ""
        return topo

            
            