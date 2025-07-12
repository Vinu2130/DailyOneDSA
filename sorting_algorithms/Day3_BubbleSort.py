# Date : 07/07/2025 (Yesterday skipped)
# Problem : Bubble sort 
# complexity : O(n^2)


def BubbleSort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        #To stop traversing through array if it is alreadysorted
        if not(swap):
            break
        # print(arr) 
    return arr

arr = [1,3,5,2,4,8,10,9]

print(f"Array elements before sorting : {arr}")
sortedArr = BubbleSort(arr)
print(f"Array elements after sorting : {sortedArr}")
