def pow(n,x):
    if x==0:
        return 1
    temp=pow(n,x//2)
    if x%2==0:
        return temp*temp
    else:
        return temp*temp*n
n=2
x=10
print(pow(n,x))
# Time Complexity: O(logN)
# Space Complexity: O(logN)


