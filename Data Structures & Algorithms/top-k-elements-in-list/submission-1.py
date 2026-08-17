class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create hash map to store count
        count = {}
        
        # Bucket to store freq hash map
        frequency = [[] for i in range(len(nums)+ 1)]

        # Loop throught count hash map TC: O(n)
        for number in nums:
            count[number] = count.get(number,0) + 1
            
      
        # Loop throught buckets and append frequency O(n) + O(1)
        for number, freqCount in count.items():
            frequency[freqCount].append(number)

        # Create output array O(n) Space
        res = []

        # Loop from end to start O(n)
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
