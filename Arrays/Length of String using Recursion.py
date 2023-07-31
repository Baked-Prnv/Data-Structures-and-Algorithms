class Solution():
    def iterative(self,str):
        leng=0
        for i in str:
            leng+=1
        return leng
    
    def recursive(self,str):
        if str == '':
            return 0
        return 1 + self.recursive(str[1:])
    
str = "GeeksforGeeks"
sol = Solution()
ans = sol.iterative(str)
print(ans)

str = "geeks"
ans = sol.recursive(str)
print(ans)