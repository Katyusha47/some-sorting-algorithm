def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sort = bubble_sort(arr)

print (sort)