# Date : 05/07/2025
# Problem : Binary Search (need a sorted array)
# complexity : O(log n)

def BinarySearch(arr,target):
    start = 0
    end = len(arr)-1
    
    while start <= end:
        mid =( end + start ) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid] :
            end = mid-1
        else:
            start = mid+1
    return -1
arr = [1,2,3,4,5,8,9,10]
target = int(input("Enter the search element: "))
target_position = BinarySearch(arr,target)

if target_position >= 0:
     print(f"The search element {target} is found at position : {target_position + 1} (i.e, at index {target_position})")
else:
    print(f"The search element is not present in the available data")