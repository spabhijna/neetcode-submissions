class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        for i in range(min(len(word1), len(word2))):
            s += word1[i] + word2[i]
        s += word1[len(word2):]
        s += word2[len(word1):]
        
        return s