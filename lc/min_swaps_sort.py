# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

def min_swaps(arr):
    temp = sorted(arr)
    dict = {}
    for index, val in enumerate(arr):
        dict[val] = index
    swap_count = 0
    for i in range(len(arr)):
        if arr[i] != temp[i]:
            swap_count += 1
            init = arr[i]
            arr[i], arr[dict[temp[i]]] = arr[dict[temp[i]]], arr[i]

            dict[init] = dict[temp[i]]
            dict[temp[i]] = i

    return swap_count


arr= [101, 758, 315, 730,
      472, 619, 460, 479]
print(min_swaps(arr))

arr = [5,1,3,2]
print(min_swaps(arr))
