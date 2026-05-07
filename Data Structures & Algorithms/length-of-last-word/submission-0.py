class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=[]
        s=s.lower()
        minNum=ord('a')
        maxNum=ord('z')
        counter=False
        for i in range(len(s)):
            if ord(s[i])<minNum or ord(s[i])>maxNum:
                counter = True
            else:
                if counter == True:
                    res.clear()
                    counter =False
                res.append(s[i])
        return len(res)