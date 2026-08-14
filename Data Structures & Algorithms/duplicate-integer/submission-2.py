class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSeen = set()
        for i in nums:
            if i in hasSeen:
                return True
            hasSeen.add(i)
        return False
        