# Date : 09/07/2025 
# Problem : Radix sort 
# complexity : O(d(n+b)) (d = no.of digits in max number in given data, n = no.of elements, b = buckets )

def find_max(arr):
    maxNum = arr[0]
    for i in arr:
        if i >= maxNum:
            maxNum = i
    return maxNum
            
def count_digits(maxNum):
    d = 0
    while maxNum > 0:
        maxNum //= 10
        d+=1
    return d
    
def RadixSort(arr):
    # step-1 : initially we need to find maximum number
    maxNum  = find_max(arr)
    
    # step-2 : find number of digits in that max number
    d = count_digits(maxNum)
    
    # step-3 : we need to sort all numbers, digit-wise
    for i in range(d):
        # step-3a: create temporary buckets for every pass
        radixDict = {k : [] for k in range(10)}

        # step-3b: inserting each element from array in their respective buckets for every pass
        for j in range(len(arr)):
            digit = (arr[j] // (10**i) )%10
            radixDict[digit].append( arr[j])
            
        # step-3b: for every pass, we need to collect sorted elements into an array and update the actual array
        newArr = []
        for num in radixDict:
            for i in radixDict[num]:
                newArr.append(i)
        arr = newArr
        
    # print(arr)  
    return arr

arr = [2001,32,57,25,143,86,10,9]

print(f"Array elements before sorting : {arr}")
sortedArr = RadixSort(arr)
print(f"Array elements after sorting : {sortedArr}")