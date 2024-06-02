class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s)==1 or len(s)==0:
            return s
        start,end=0,len(s)-1
        while start<end:
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
        return s