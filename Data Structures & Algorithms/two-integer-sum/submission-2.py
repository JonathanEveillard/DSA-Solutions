class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dict/hashmap to store value key/index
        prevMap = {}
        for i, k in enumerate(nums):
            prevMap[k] = i
    
        # Verify
        for i, k in enumerate(nums):
            val = target - k
            if val in prevMap and prevMap[val] != i:
                return [i, prevMap[val]]
        return None