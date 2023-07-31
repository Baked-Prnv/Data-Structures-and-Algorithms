"""509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
That is, F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2), for n > 1. Given n, calculate F(n).
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3."""

class Solution():
    def fib(self, num):
        if num == 0:
            return 0
        if num == 1:
            return 1
        
        return self.fib(num-1)+self.fib(num-2)
    
sol = Solution()
ans = sol.fib(9)
print(ans)