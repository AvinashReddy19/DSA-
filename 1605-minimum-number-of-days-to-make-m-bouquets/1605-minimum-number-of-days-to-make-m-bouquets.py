class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(arr,day,m,k):
            counter,no_of_bouquets=0,0
            for i in range(len(arr)):
                if arr[i]<=day:
                    counter+=1
                else:
                    no_of_bouquets+=counter//k
                    counter=0
            no_of_bouquets+=counter//k
            if no_of_bouquets>=m:
                return True
            else:
                return False
        def binarySearch(arr,m,k):
            low=min(arr)
            high=max(arr)
            while low<=high:
                mid=low+(high-low)//2
                if possible(arr,mid,m,k):
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        if m*k>len(bloomDay):
            return -1
        return binarySearch(bloomDay,m,k)