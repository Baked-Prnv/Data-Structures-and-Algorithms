"""Quick Sort
It is based on divide and conquer algorithm, that picks an element as a pivot and partitions the given array 
around pivot by placing pivot in its correct position in sorted array. put all the smaller elements to the left of pivot
and all greater to the right of pivot. partition is done recursively on each side of pivot after the pivot is placed
in its correct position.
"""

class Solution():
    def quickSort(self, arr, left, right):

        def partition(arr, left, right):
            i = left
            j = right -1
            pivot = arr[right]
            while i<j:
                while i<right and arr[i]<pivot:
                    i+=1
                while j>left and arr[j]>=pivot:
                    j-=1
                if i<j:
                    arr[i],arr[j]=arr[j],arr[i]
            if arr[i]>pivot:
                arr[i],arr[right]=arr[right],arr[i]
            return i
        
        if left<right:
            pivot_pos = partition(arr,left,right)
            self.quickSort(arr,left,pivot_pos-1)
            self.quickSort(arr,pivot_pos+1,right)
        return arr


arr = [22,11,88,66,55,77,33,44]
sol = Solution()
ans = sol.quickSort(arr,0,len(arr)-1)
print(arr)