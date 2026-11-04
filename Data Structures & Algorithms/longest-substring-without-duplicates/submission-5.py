class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        seenChar = []
        counterList = []
        counter = 0
        for charIndex in range(len(s)):
            if s[charIndex] not in seenChar:
                counter += 1
                seenChar.append(s[charIndex])
            elif charIndex == (len(s) - 1):
                counterList.append(counter)
            else:
                counterList.append(counter)
                counter = 1
                seenChar = [s[charIndex]]

        return max(counterList)
                
        