class Solution(object):
    def findPeakElement(self, nums):
        b=0
        c=max(nums)
        for i in range(len(nums)):             
            if c==nums[i]:
                return i
