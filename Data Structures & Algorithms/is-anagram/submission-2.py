#SC: O(1)
#TC: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        # Init fixed arr size for count
        count = [0] * 26
        
        # Ensure that s,t are lower O(n)
        s.lower()
        t.lower()

        # Increments character val 
        for ch in s:
            count[ord(ch) - ord('a')] +=1
        
        # Decrements character val 
        for ch in t:
            count[ord(ch) - ord('a')] -=1

        # Verify anagram by character val == 0
        for c in count:
            if c != 0:
                return False

        return True


        