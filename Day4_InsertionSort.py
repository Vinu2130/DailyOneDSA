# Date : 07/07/2025 
# Problem : selection sort 
# complexity : O(n^2)

def InsertionSort(arr):
    for i in range(1,len(arr)-1):
        j = i + 1
        while (j > 0 and arr[j-1] > arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
        # print(arr)
    return arr
arr = [1,3,5,2,4,8,10,9]

print(f"Array elements before sorting : {arr}")
sortedArr = InsertionSort(arr)
print(f"Array elements after sorting : {sortedArr}")