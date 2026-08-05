class Solution(object):
    def findKthLargest(self, nums, k):
        """def maxx(nums):
            a=nums[0]
            b=0
            for i in range(len(nums)):
                if nums[i]>a:
                    a=nums[i]
                    b=i
            return a 
        c=1
        a=0
        i=0
        for i in range(k-1):
            a=maxx(nums)
            nums.remove(a)
        return max(nums)"""

        nums.sort()
        return nums[len(nums)-k]
            

        