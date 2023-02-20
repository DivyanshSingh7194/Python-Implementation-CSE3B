def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        
        pivot = arr[-1]
        
        left = [elem for elem in arr[:-1] if elem <= pivot]
        right = [elem for elem in arr[:-1] if elem > pivot]
        
        return quick_sort(left) + [pivot] + quick_sort(right)


arr = [64, 25, 12, 22, 11]
result = quick_sort(arr)
print(result)
