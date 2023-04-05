def cocktail_shaker_sort(arr):
    is_sorted = True
    while is_sorted:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = True

        if not is_sorted:
            break

        is_sorted = False

        for j in range(len(arr) - 1, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                is_sorted = True

    return arr

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = cocktail_shaker_sort(arr)
print(sorted_arr)
