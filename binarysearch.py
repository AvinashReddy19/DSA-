# conditions:    low<=high  and must be in monotonic function which is either increasing or decreaing 
# time complexity : O(logN)

def binarysearch(arr,key):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=high+(low-high)//2
        if arr[mid]==key:
            return mid
        else:
            if arr[mid]>key:
                high=mid-1
            else:
                low=mid+1
    return -1

arr=[1,2,3,4,5,6,7,8,9,10]
key=5
print(binarysearch(arr,key))
            
    