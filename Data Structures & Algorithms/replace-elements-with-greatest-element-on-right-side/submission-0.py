class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[]
        rightMax=-1
        for i in range(n-1,-1,-1):
            res.append(rightMax)
            rightMax=max(rightMax, arr[i])
        return res[::-1]