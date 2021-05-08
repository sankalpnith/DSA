# https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/

# Given a boolean 2D array of n x m dimensions where each row is sorted.
# Find the 0-based index of the first row that has the maximum number of 1's.

def rowWithMax1s(arr, n, m):
        row_index = -1
        # for i in range(m):
        #     if arr[0][i] == 1:
        #         row_index = 0
        #         col_index = i
        #         break
        # if col_index is None:
        #     col_index = m-1
        col_index = m-1
        for i in range(n):
            while col_index >= 0 and arr[i][col_index] == 1:
                col_index -= 1
                row_index = i
        return row_index

n1 = [0,1,1,1]
n2 = [0,0,1,1]
n3 = [1,1,1,1]
n4 = [0,0,0,1]
arr =[]
arr.append(n1)
arr.append(n2)
arr.append(n3)
arr.append(n4)
print(rowWithMax1s(arr, 4, 4))