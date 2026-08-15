class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Hashmap to store anagram groups
        prevMap = defaultdict(list)
        
        # Character Frequency per string
        for s in strs:

            # Init count to lower case 26 letters
            count = [0] * 26
            
            # Character count frequency
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Tuple hashable key for frequency signature
            key = tuple(count)
            prevMap[key].append(s)
        
        return list(prevMap.values())