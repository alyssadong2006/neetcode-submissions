class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        lengthList = [0]
        seen = []

        for i in range(len(s)):
            # print(f'Index: {i}, Char: {s[i]}')
            if s[i] not in seen:
                seen.append(s[i])
            else:
                lengthList.append(i - sum(lengthList))
                seen = [s[i]]
            # print(seen)
            # print(lengthList)

        return max(lengthList)



                
        