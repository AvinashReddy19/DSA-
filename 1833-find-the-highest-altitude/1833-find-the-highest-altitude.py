class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ar=[0]
        l=0
        for i in gain:
            k=ar[l]+i
            ar.append(k)
            l+=1
        return max(ar)