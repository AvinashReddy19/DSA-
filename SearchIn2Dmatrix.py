# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# [1,3,5,7]
# [10,11,16,20]
# [23,30,34,60]                  key=3 if present return True else False

def searchIn2d(matrix, key):
    n = len(matrix)
    m = len(matrix[0])
    
    # Binary search in the first column to find the possible row
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if matrix[mid][0] == key:
            return True
        elif matrix[mid][0] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    # If the key is not found in the first column, set the row to high
    row = high
    
    # Binary search in the selected row to find the key
    low = 0
    high = m - 1
    while low <= high:
        mid = low + (high - low) // 2
        if matrix[row][mid] == key:
            return True
        elif matrix[row][mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

arr = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
key = 3
print(searchIn2d(arr, key))

    