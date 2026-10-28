class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for char in s:
                counter[ord(char) - ord('a')] += 1
        
            wordDict[tuple(counter)].append(s)
        
        return list(wordDict.values())
        