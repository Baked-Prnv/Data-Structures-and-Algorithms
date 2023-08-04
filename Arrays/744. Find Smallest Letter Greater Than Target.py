"""744. Find Smallest Letter Greater Than Target
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0]."""


class Solution():
    def greaterChar(self,letters, target):

        l,r = 0,len(letters)-1
        if target<letters[l] or target>=letters[r]:
            return letters[l]
        
        while l<=r:
            m = (l+r)//2
            if target<letters[m]:
                r = m-1
            else:
                l = m+1
                
        return letters[l]
    

print(Solution().greaterChar(letters = ["x","x","y","y"],target = "z"))             #x

print(Solution().greaterChar(letters = ["c","f","j"],target = "c"))                 #f

print(Solution().greaterChar(letters = ["c","f","j"],target = "a"))                 #c