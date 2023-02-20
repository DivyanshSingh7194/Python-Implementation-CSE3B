def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [1, 3, 5, 7, 9]
x = 5
result = linear_search(arr, x)
result1 = linear_search(arr,7)
print(result)
print(result1)
