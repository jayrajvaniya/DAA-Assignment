class Solution(object):
    def sortArray(self, nums):
        def mergs(num,l,h,mid):
            result=[]
            left=nums[l:mid+1]
            right=nums[mid+1:h+1]
            i=0
            j=0
            k=l
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    nums[k]=left[i]
                    i+=1
                else:
                    nums[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1
            return result
        def mergesort(nums,l,h):
            if l==h:
                return 
            mid=l+(h-l)//2
            mergesort(nums,l,mid)
            mergesort(nums,mid+1,h)
            mergs(nums,l,h,mid)
        mergesort(nums,0,len(nums)-1)
        return nums    