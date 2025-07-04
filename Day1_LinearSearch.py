# Date : 04/07/2025
# Problem : Linear Search
# complexity : O(n)

def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


arr = [1,3,5,2,4,8,10,9]
target = int(input("Enter the search element: "))
target_position = LinearSearch(arr,target)

if target_position:
    print(f"The search element {target} is found at position : {target_position + 1}")
else:
    print(f"The search element is not present in the available data")


