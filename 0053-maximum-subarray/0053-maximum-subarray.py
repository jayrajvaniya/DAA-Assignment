class Solution(object):
    def maxSubArray(self, nums):
        a=nums[0]
        s=0
        for i in nums:
            if s<0:
                s=0
            s+=i
            a=max(a,s)
        return a
        