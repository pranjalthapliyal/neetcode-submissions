class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s)<=0:
            return 0
        res=0
        j=1
        for i in range(len(s)-1):
            res += abs(ord(s[i]) - ord(s[j]))
            j+=1
        return res