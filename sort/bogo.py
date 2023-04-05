import random

def bogosort(arr):
    while not sorted(arr):
        arr = shuffle(arr)
    return arr

def shuffle(arr):
    m = len(arr)
    while m:
        m -= 1
        i = random.randint(0, m)

        # swap values at positions i and m
        arr[i], arr[m] = arr[m], arr[i]

    return arr

def sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = bogosort(arr)
print(sorted_arr)
