class Solution:
    # Code
    # [Hello, World]
    # num,num,num,num,num,sum,num,num ...,sum

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            # sum of the unicode of the word
            sum = 0

            for letter in string:
                unicode = ord(letter)
                sum += unicode
                s += f'{unicode},'
            
            s += f'{sum},'
        
        return s

    def decode(self, s: str) -> List[str]:
        unicodeList = s.split(",")
        unicodeList.remove("")
        # print(unicodeList)
        string = ""
        stringList = []
        unicodeSum = 0
        for unicode in unicodeList:
            unicode = int(unicode)
            # print(f'Unicode:{unicode}\nSum:{unicodeSum}\n')
            if unicodeSum != unicode:
                string += chr(unicode)
                unicodeSum += unicode
            else:
                # print("Ran")
                stringList.append(string)
                string = ""
                unicodeSum = 0
        
        return stringList


