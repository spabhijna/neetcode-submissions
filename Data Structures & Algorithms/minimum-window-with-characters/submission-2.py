class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''

        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c,0) + 1
        
        have, need = 0, len(countT)
        result = [-1,-1]
        resL = float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resL:
                    result = [l,r]
                    resL = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = result

        return s[l:r+1] if resL != float('inf') else ''

        
        
        