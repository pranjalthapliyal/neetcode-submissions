class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter=0
        for i in range(len(details)):
            age = details[i][11:13]
            if int(age)>60:
                counter+=1
        return counter 