import sys

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
    
    def largeNumFactorial(self, num): 
                                        #for larger numbers
        def multiply(n,res,res_size):
            carry = 0
            i=0
            while i < res_size:
                prod = n*res[i]+carry
                carry = prod//10
                res[i]= prod%10
                i+=1

            while carry:
                res[res_size]= carry%10
                carry //= 10
                res_size += 1

            return res_size
                
        res = [None]*500
        res[0],res_size=1,1
        x=2
        while x<=num:
            res_size =multiply(x,res,res_size)
            x+=1
       
        i = res_size-1
        while i >= 0:
            sys.stdout.write(str(res[i]))
            sys.stdout.flush()
            i = i - 1
        
    
sol =Solution()
ans = sol.fac(6)
print(ans)

sol.largeNumFactorial(200)
