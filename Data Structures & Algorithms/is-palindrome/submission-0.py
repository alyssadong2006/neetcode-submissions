class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum())
        clean = clean.lower()
        length = len(clean)

        print(clean)
        if length % 2 == 0:
            # print(clean[:length//2])
            return (clean[:length//2] == clean[length-1:length//2:-1])
        else:
            length -= 1
            # print(clean[:length//2])
            # print(clean[length:length//2:-1])
            return(clean[:length//2] == clean[length:(length//2):-1])
        