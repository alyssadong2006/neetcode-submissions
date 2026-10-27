class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}

        for letter in s:
            if letter not in sDict.keys():
                sDict[letter] = 1
            else:
                sDict[letter] += 1
        
        for letter in t:
            if letter in sDict.keys():
                sDict[letter] -= 1
            else:
                sDict[letter] = -1
        
        return all(value == 0 for value in sDict.values())
        