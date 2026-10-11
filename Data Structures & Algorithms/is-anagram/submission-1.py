class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            s1=''.join(sorted(s.lower()))
            t1=''.join(sorted(t.lower()))
            for i, j in zip(s1, t1):
                if i==j:
                    continue
                else:
                    return False
            return True
            
        