class Solution:
    def minOperations(self, logs: List[str]) -> int:
        newDict = {"../":-1, "./":0}
        counter = 0
        for log in logs:
            if log in newDict:
                counter+= newDict[log]
            else:
                counter+=1
            counter = 0 if counter<=0 else counter
        return counter
        