# Date : 08/07/2025 
# Problem : Selection sort 
# complexity : O(n^2)

def SelectionSort(arr):
    for i in range(len(arr)-1):
        currentMinIndex = i
        for j in range(i+1,len(arr)):
            if (arr[j] < arr[currentMinIndex]):
                currentMinIndex = j
        if currentMinIndex != i:
            arr[currentMinIndex],arr[i] = arr[i],arr[currentMinIndex]
        # print(arr)
    return arr

arr = [1,3,5,2,4,8,10,9]

print(f"Array elements before sorting : {arr}")
sortedArr = SelectionSort(arr)
print(f"Array elements after sorting : {sortedArr}")