# Approach Top-down dp, 

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize variables to represent the maximum profit
        # for the previous house and the house before the previous house
        prev, next = 0, 0
        
        # Iterate over the list of house values
        for i in nums:
            # Calculate the maximum profit for the current house
            # by considering the sum of the profit from robbing the previous house
            # and the profit from skipping the previous house and robbing the house before it
            temp = max(prev + i, next)
            
            # Update the variables for the next iteration
            prev = next
            next = temp
        
        # The final result is the maximum profit achievable
        # considering all the houses in the given list
        return next


# Recursion + Memoization Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def helper(i):
            if i < 0:
                return 0
            if i not in cache:
                next = nums[i] + helper(i - 2)
                prev = helper(i - 1)
                cache[i] = max(prev, next)
            return cache[i]

        return helper(len(nums) - 1) 
