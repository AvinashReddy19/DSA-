# input: [0,1,2,2,2,2,2,3]
# key=2
# o/p: 2,6

# Solution:
# 1. Find the first occurence of the key // LEFT MOST INDEX
# 2. Find the last occurence of the key   // RIGHT MOST INDEX
# 3. Return the first and last occurence of the key

def firstAndLastPosition(arr, n, k):

    # Write your code here
    low=0
    ans1=-1
    high=len(arr)-1
    
    while low<=high:
        mid=high+(low-high)//2
        if arr[mid]==key:
            ans1=mid
            high=mid-1
    

        elif arr[mid]>key:
            high=mid-1

        else:
            
            low=mid+1

    low=0
    high=len(arr)-1
    ans2=-1
    
    while low<=high:
        mid=high+(low-high)//2
        if arr[mid]==key:
            ans2=mid
            low=mid+1
    

        elif arr[mid]>key:
            high=mid-1

        else:
            
            low=mid+1
    
    return ans1,ans2



arr=[0,1,2,2,2,2,2,3]
key=2
print(firstAndLastPosition(arr,len(arr),key))