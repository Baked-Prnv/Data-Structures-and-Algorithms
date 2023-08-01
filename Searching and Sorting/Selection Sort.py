"""Selection Sort
It works by repeatedly selecting the smallest (or largest) element from unsorted portion of the list and moving it to the sorted portion of the list.
swapping it with first element of unsorted part.
Advantages
    it never makes more than O(n) swaps and can be useful when memory writing is costly.
    works well with small datasets.
    simple and easy to understand.
Disadvantages
    Does not preserve relative order of items with equal keys which means it is not stable.
"""

class Solution():

    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1,len(arr)):
                if arr[min_idx]>arr[j]:
                    min_idx = j

            arr[i],arr[min_idx]=arr[min_idx],arr[i]

        return arr

arr = [64, 25, 12, 22, 11]
sol =Solution()
ans = sol.selectionSort(arr)
print(ans)                      #[11, 12, 22, 25, 64]