class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        maxLen = 0

        for right, char in enumerate(s):
            if char in charMap:
                left = charMap[char] + 1
            charMap[char] = right
            maxLen = max(maxLen, right - left + 1)

        return maxLen


                
        