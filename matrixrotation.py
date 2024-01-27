# [1,2,3]                [7, 4, 1] 
# [4,5,6]    ----->      [8, 5, 2]
# [7,8,9]                [9, 6, 3]

def matrixrotation(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(n):
        arr[i].reverse()
    return arr
arr=[[1,2,3],[4,5,6],[7,8,9]]
print(matrixrotation(arr))
# Time Complexity: O(N^2)
# Space Complexity: O(1)
  