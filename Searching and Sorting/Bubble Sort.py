"""Bubble Sort
It works by repeatedly swapping the adjacent element if they are in wrong order.
Not suitable for large datasets as its average and worst-case time complexity is high.
Advantages: 
    Easy to understand, 
    Doesn't require any additional space, 
    Stable sorting Algorithm i.e., elements with same key value maintain their relative order in sorted output
Disadvantages:
    Slow for large dataset bcz of the o(n^2) time complexity
    Comparision-based algorithm, i.e., requires a comparison operator to determine the relative order of elements in the input data set. 
    It can limit the efficiency of the algorithm in certain cases.    
"""

class Solution():
    
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n):
            swapped = False
            
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped = True
            
            if swapped == False:
                break

        return arr

arr = [64, 34, 25, 12, 99, 22, 11, 90]
sol = Solution()
ans = sol.bubbleSort(arr)
print(arr)