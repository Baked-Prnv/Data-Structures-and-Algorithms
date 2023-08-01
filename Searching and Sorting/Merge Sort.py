"""Merge Sort
It works by dividing the array into smaller subarray, and sorting each subarray and merging sorted subarray.
it is a recursive algorithm that continuously splits the array in half until it can't be divided
i.e., array with only 1 element left (and 1 element is always sorted), then sorted subarray are merged into one sorted array.
Advantages
    well-suited for large datasets with worst case time complexity as O(nlogn)
    adaptive to handle partially sorted, nearly sorted and completely unsorted
    stable sorting algorithm i.e., it maintains the relative order of equal elements in input array.
Disadvantages
    requires additional memory to store the merged subarray during process.
    for small datasets, it has higher time complexity than other like insertion sort.
"""

class Solution():
    def mergeSort(self,arr):
        if len(arr)>1:
            L = arr[:len(arr)//2]
            R = arr[len(arr)//2:]

            self.mergeSort(L)               #sorting 1st half
            self.mergeSort(R)               #sorting 2nd half

            i=j=k=0                         #left_arr_idx, right_arr_idx, Merge_arr_idx
            while i<len(L) and j<len(R):    #merging from L[] and R[]
                if L[i]<R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1

            while i<len(L):                 #checking if any element left in L
                arr[k] = L[i]
                i+=1
                k+=1
            
            while j<len(R):                 #checking if any element left in R
                arr[k] = R[j]
                j+=1
                k+=1

        return arr
    
arr = [12, 11, 13, 5, 6, 7]
sol = Solution()
ans =sol.mergeSort(arr)
print(ans)                              #[5, 6, 7, 11, 12, 13]

arr = [7,3,5,3,1,0,1,8,5,8,4]
ans =sol.mergeSort(arr)
print(ans)                              #[0, 1, 1, 3, 3, 4, 5, 5, 7, 8, 8]