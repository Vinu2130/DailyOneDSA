# Date : 11/07/2025 
# Problem : Quick Sort
# complexity : O(nlogn)

def QuickSort(arr,l ,r):
    if l < r:
        pivot_position = Partition(arr,l,r)
        QuickSort(arr,l,pivot_position)
        QuickSort(arr,pivot_position+1,r)
    return arr
def Partition(arr,l,r):
    pivot = arr[l]
    left = l+1
    
    for i in range(l+1,r):
        if arr[i] < pivot:
            arr[i],arr[left] = arr[left],arr[i]
            left+=1
    arr[l],arr[left-1] = arr[left-1],arr[l]
   
    return left-1
        

arr = [1,3,5,2,4,8,10,9]

print(f"Array elements before sorting : {arr}")
sortedArr = QuickSort(arr,0,len(arr)-1)
print(f"Array elements after sorting : {sortedArr}")