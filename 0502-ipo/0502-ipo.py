class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        cp = list(zip(capital, profits))
        cp.sort()

        pq=[]
        curr=0
        for i in range(k):
            while curr<n and cp[curr][0]<=w:
                heapq.heappush(pq, -cp[curr][1])
                curr+=1
            if pq: w-=heapq.heappop(pq)
            else: break
        return w
        