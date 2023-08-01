"""Insertion Sort
Array is virtually split into sorted and unsorted part.
Value from unsorted part is picked and placed at the correct position in the sorted part.
Advantages:
    Efficient for the small data values
    Adaptive in nature, i.e., appropriate for datasets that are already partially sorted."""

class Solution():

    def insertionSort(self, arr):
        
        for i in range(1, len(arr)):
            key = arr[i]

            j = i-1
            while j>=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            
            arr[j+1] = key

        return arr

arr = [12,39,24,2,7,22, 11, 13, 5, 6]
sol = Solution()
ans = sol.insertionSort(arr)
print(ans)                                  #[2, 5, 6, 7, 11, 12, 13, 22, 24, 39]

