def partition(arr, p, r):
    x = arr[p]
    i = p
    for j in range(p + 1, r + 1):
        if(arr[j] < x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[p] = arr[p], arr[i]
    return i


def Quicksort(arr, p, r):
    while(p < r):
        q = partition(arr, p, r)
        Quicksort(arr, p, q - 1)
        p = q + 1


arr = [5, 4, 2, 7, 9, 6, 8]
print(arr)
Quicksort(arr, 0, len(arr) - 1)

print(arr)
