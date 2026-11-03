class Solution:
    """
    After thought:
        Encoding Method:
            - if list is empty, just return an empty string
            - first few numbers be the length of a word with a comma in between
            - seperate with special character
            - add long list of strings from the words combined
            - return the long string with "{sizes}{specialChar}{jumbleOfWords}"

        Decoding Method:
            - if string is empty, return empty list
            - split with the first occurence of the special character: {encodedString}.split({specialChar, 1})
            - sizeList -> [0].split(",") to get list of diff sizes
            - wordList -> [1], the jumble of words together
            - iterate through sizeList to cut out words in the wordList
            - append the words into return list
    """

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
            
