class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        stringSizes = []
        wordStrings = ""
        for s in strs:
            stringSizes.append(len(s))
            wordStrings += s
        
        coded = "".join([f'{size},' for size in stringSizes])
        coded += "#"
        coded += wordStrings

        return coded


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
            
        infoList = s.split("#", 1)
        sizeList = infoList[0].split(",")
        sizeList.remove("")
        wordList = infoList[1]

        decoded = []
        currIndex = 0
        for size in sizeList:
            # print(f"{wordList[currIndex:]}, {size}")
            string = wordList[currIndex:currIndex + int(size)]
            currIndex += int(size)
            decoded.append(string)
        
        return decoded
            
