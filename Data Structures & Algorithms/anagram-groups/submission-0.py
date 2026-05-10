class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for word in strs:
            wordList = [0]*26
            for char in word:
                charIndex = ord(char) - ord('a')
                wordList[charIndex] += 1
            key = tuple(wordList)
            print(key, word)
            if key in res:
                res[key].append(word)
            else:
                res[key]=[word]
        return list(res.values())
        