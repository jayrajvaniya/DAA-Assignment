class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def mul(n):
            a=1
            while n>0:
                q=n%10
                a*=q
                n=n//10
            return a
        for i in range(n,n+10):
            if mul(i)%t==0:
                return i
        
        