# https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/

# Given a boolean 2D array of n x m dimensions where each row is sorted.
# Find the 0-based index of the first row that has the maximum number of 1's.

def rowWithMax1s(arr, n, m):
        col_index = None
        row_index = -1
        for i in range(n):
            for j in range(m):
                if col_index is None:
                    if arr[i][j] == 1:
                        row_index = i
                        col_index = j
                        break
                else:
                    if arr[i][col_index-1] == 1:
                        if arr[i][j] == 1:
                            row_index = i
                            col_index = j
                            break
                    else:
                        break
            if col_index == 0:
                return row_index
        return  row_index

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