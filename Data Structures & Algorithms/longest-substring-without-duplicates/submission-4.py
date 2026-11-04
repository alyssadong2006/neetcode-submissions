class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        seenChar = []
        counterList = []
        counter = 0
        for char in s:
            if char not in seenChar:
                counter += 1
                seenChar.append(char)
            else:
                counterList.append(counter)
                counter = 1
                seenChar = [char]

        return max(counterList)
                
        