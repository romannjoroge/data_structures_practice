"""
Docstring for Leetcode.Python.question_35

Problem link: https://leetcode.com/problems/search-insert-position/ 
"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        We're looking for the point that's either equal to the target or just 
        more than it

        is_point(x) = true, if nums[x] == target
                    = true, if nums[x] > target and nums[x-1] < target
                    = false, if nums[x] < target [below case]
                    = false, if nums[x] > target and nums[x-1] > target [above case]
        """
        # Make lower range 0 and higher range length of nums - 1
        low = 0
        high = len(nums) - 1

        # while true
        while True:
            if low >= len(nums):
                return len(nums)
            elif high <= -1:
                return 0
            
            middle = (low + high) // 2
            # Test if middle is target
            if nums[middle] == target or (nums[middle] > target and nums[middle - 1] < target):
                # If target return middle
                return middle
            # Else if above case change high to middle
            elif nums[middle] > target and nums[middle - 1] >= target:
                high = middle - 1
            # Else change low to middle
            else: 
                low = middle + 1

            
            
        
            
            
        