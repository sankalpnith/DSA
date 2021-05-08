

def transpose(arr):
    print(arr)
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    print(arr)
    return arr

def rotate_90_clockwise(arr):
    for i in range(len(arr)):
        j = 0
        k = len(arr) - 1
        while j < k:
            arr[i][j], arr[i][k] = arr[i][k], arr[i][j]
            j += 1
            k -= 1
    print(arr)
    return arr

def rotate_90_anticlockwise(arr):
    for i in range(len(arr)):
        j = 0
        k = len(arr) -1
        while j<k:
            arr[j][i], arr[k][i] = arr[k][i], arr[j][i]
            j += 1
            k -=1
    print(arr)
    return arr

a1 = [1,2,3,4]
a2 = [5,6,7,8]
a3 = [9,10,11,12]
a4 = [13,14,15,16]
arr = []
arr.append(a1)
arr.append(a2)
arr.append(a3)
arr.append(a4)
transpose(arr)
# rotate_90_anticlockwise(arr)
rotate_90_clockwise(arr)

# reverse 90- clockwise -> transpose and reverse elements in each row
# reverse 90- anticlockwise -> transpose and reverse elements in each column
# 180 rotation -> reverse elements in each row and reverse columns in each row
