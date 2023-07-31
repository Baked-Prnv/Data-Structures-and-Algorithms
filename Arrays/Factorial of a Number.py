class Solution():

    def factorial(self,num):        #recursion
        if num == 1:
            return 1
        return num* self.factorial(num-1)
    
    def fact(self, num):            #iteration
        res=1
        for i in range(2,num+1):
            res*=i
        return res
    
    def fac(self,n):                #one liner
        return 1 if (n==1 or n==0) else n*self.fac(n-1)
    
sol =Solution()
ans = sol.fac(6)
print(ans)
