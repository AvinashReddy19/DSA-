# arr=[2,1,5,4,3,0,0]
# o/p: [2,3,0,0,1,4,5]

# BF:  
#   1. generate all possible subsets 
#   2. linear search the given array                                     time complexity: O(N!*N)
#   3. print the next indexed array

#optimal

def permutation(arr):
    ind=-1
    for i in range(len(arr)-2,0,-1):
        if arr[i]<arr[i+1]:
            ind=i
            break
    if ind==-1:
        arr.reverse()
        return arr
    for i in range(len(arr)-1,ind,-1):
        if arr[i]>arr[ind]:
            arr[i],arr[ind]=arr[ind],arr[i]
            break
    arr[ind+1:]=arr[ind+1:][::-1]
    return arr

arr=[2,1,5,4,3,0,0]
print(permutation(arr))
# Time Complexity: O(N)
# Space Complexity: O(1)
