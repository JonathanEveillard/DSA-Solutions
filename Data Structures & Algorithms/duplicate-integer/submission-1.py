class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       
        # Empty Set
        seen = set()
        
        # Verify if element is in set & return true
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        # Return false
        return False 
        