# Date : 11/07/2025 (Yesterday skipped)
# Problem : Merge Sort
# complexity : O(nlogn)

def MergeSort(arr):
    if len(arr) == 1:
        return arr
    
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]
    # print(arr1)
    # print(arr2)
    
    arr1 = MergeSort(arr1)
    arr2 = MergeSort(arr2)
    
    return Merge(arr1,arr2)

def Merge(arr1,arr2):
    sortedArr = []
    while(arr1 and arr2):
        if(arr1[0] > arr2[0]):
            sortedArr.append(arr2[0])
            arr2.remove(arr2[0])
        else:
            sortedArr.append(arr1[0])
            arr1.remove(arr1[0])
    while arr1:
        sortedArr.append(arr1[0])
        arr1.remove(arr1[0])
    while arr2:
        sortedArr.append(arr2[0])
        arr2.remove(arr2[0])
    # print(sortedArr)
    return sortedArr

arr = [1,3,5,2,4,8,10,9]

print(f"Array elements before sorting : {arr}")
sortedArr = MergeSort(arr)
print(f"Array elements after sorting : {sortedArr}")