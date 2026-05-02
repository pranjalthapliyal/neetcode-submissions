class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=[]
        n=2
        for i in range(2):
            for j in range(len(nums)):
                res.append(nums[j])
        return res
