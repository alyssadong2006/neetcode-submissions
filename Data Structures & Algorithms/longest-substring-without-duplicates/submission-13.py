class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        maxLen = 0
        for right, char in enumerate(s):
        # right is the index, char is the character in s
            if char in charMap and charMap[char] >= left:
            # if character has been seen before and 
            # was the last time we've seen the char at or 
            # after left boundary
                left = charMap[char] + 1
            charMap[char] = right
            # update each characters most right position
            maxLen = max(maxLen, right - left + 1)
            # update max length 

        return maxLen


                
        