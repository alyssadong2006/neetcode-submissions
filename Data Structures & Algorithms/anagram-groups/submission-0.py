class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initializes a hash map where keys auto default to [] if they dont exist
        res = defaultdict(list)
        for word in strs:
            # creates a 26 sized list of zeroes to count each lowercase letter
            count = [0] * 26
            for letter in word:
                # ord() returns unicode of a character
                # ord(letter) - ord('a') gives the index we want to point to
                # += 1 adds to the count
                count[ord(letter) - ord('a')] += 1
            # for each word, we get a list of 26 items that shows the counter for
            # each letter within the word

            # using the tuple ver of the counter list as a key, we append
            # the corresponding word to the list of values
            res[tuple(count)].append(word)
        # we then return a list of only the values in the dict
        return list(res.values())
        