# TC: O(n) SC:O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dict/hashmap to store value key/index
        prevMap = {}
        for k, v in enumerate(nums):
            prevMap[v] = k
    
        # Verify
        for k, v in enumerate(nums):
            val = target - v
            if val in prevMap and prevMap[val] != k:
                return [k, prevMap[val]]
        return None