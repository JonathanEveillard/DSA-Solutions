class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Find frequency count with a hash 
        freq = {}

        for num in nums:
            if num in freq:
                # Already exist - Increment count
                freq[num]+=1 
            else:
                # Init to 1
                freq[num]=1

        buckets = [[] for _ in range(len(nums)+1)] # Init Bucket Arr
        res = [] # Result Arr

        # Place val into bucket
        for num in freq:
            count = freq[num]
            buckets[count].append(num)
        
        # Return Res
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
