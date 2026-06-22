class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # Init result

        # strings with proper format 
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # initialization
        res = []
        i = 0

        while i < len(s):
            j = i

            # Increment j, if delimiter hasn't hit
            while s[j] != "#":
                j += 1

            length = int(s[i:j]) # Length Slice
            word = s[j+1 : j+1+length] # Word Slice
            res.append(word)

            # Increment i to next string
            i = j+1+length
        return res