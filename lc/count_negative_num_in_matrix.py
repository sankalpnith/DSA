# https://www.geeksforgeeks.org/count-negative-numbers-in-a-column-wise-row-wise-sorted-matrix/
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
def calculate(arr, m, n):
    row = 0
    col = n-1
    count = 0
    while col >=0 and row < m:
        if arr[row][col] < 0:
            count += col + 1
            row += 1
        else:
            col -= 1
    return count

n1 = [-3,-2,-1,0]
n2 = [-2,2,3,4]
n3 = [4,5,7,8]
arr =[]
arr.append(n1)
arr.append(n2)
arr.append(n3)
print(calculate(arr, 3, 4))

