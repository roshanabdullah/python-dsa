# using recursion + dp
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        cache = []

        def helper(n):
            if(not n):
                return 0
            
            cache = n
            if cache == nums:
                return nums + cache
            
                

        return helper(nums)
            
        
