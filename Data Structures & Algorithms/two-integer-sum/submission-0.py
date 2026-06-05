class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}

        # i -> key/position in dict (where it is in the hashmap)
        # j -> value in dict (actual data)
        for i, j in enumerate(nums):
            val = target - j 

            if val in map:
                # returns index position of sum value
                return [map[val],i]
            map[j] = i
        return []