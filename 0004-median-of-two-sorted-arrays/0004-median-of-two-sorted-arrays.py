class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def merge(nums1,nums2,m,n):
            i=0
            j=0
            re=[]
            while i<m and j<n:
                if nums1[i]<=nums2[j]:
                    re.append(nums1[i])
                    i+=1
                else:
                    re.append(nums2[j])
                    j+=1
            while i<m:
                re.append(nums1[i])
                i+=1
            while j<n:
                re.append(nums2[j])
                j+=1
            return re
        c=merge(nums1,nums2,len(nums1),len(nums2))
        d=len(c)
        if d%2==0:
            n=int((d/2)-1)
            return (c[n]+c[n+1])/2.0
        else:
            n=int((d+1)/2)
            return c[n-1]
        
        