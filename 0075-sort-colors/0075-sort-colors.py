class Solution:
    def sortColors(self, arr: List[int]) -> None:
        start,mid=0,0
        end=len(arr)-1
        while mid <= end:
            if arr[mid] == 0:
                arr[start], arr[mid] = arr[mid], arr[start]
                start += 1
                mid += 1
            elif arr[mid] == 2:
                arr[mid], arr[end] = arr[end], arr[mid]
                end -= 1
            else:  # arr[mid] == 1
                mid += 1

        return arr
                
