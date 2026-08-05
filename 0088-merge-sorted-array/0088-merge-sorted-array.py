class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """for i in range(0,n):
            nums1[m+i]=nums2[i]
        nums1.sort()
        return nums1 """
        def mergs(num1,num2,start,end):
            result=[]
            i=0
            j=0
            while i<start and j<end:
                if num1[i]<=num2[j]:
                    result.append(num1[i])
                    i+=1
                else:
                    result.append(num2[j])
                    j+=1
            while j<end:
                result.append(num2[j])
                j+=1
            while i<start:
                result.append(num1[i])
                i+=1
            return result
        r=mergs(nums1,nums2,m,n)
        nums1[:]=r[:]