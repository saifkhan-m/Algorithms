def partition(arr, p, r):
    x = arr[p]
    i = p
    for j in range(p + 1, r + 1):
        if(arr[j] > x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[p] = arr[p], arr[i]
    return i


def select(arr, p, r, i):
    if p == r:
        return arr[p]
    q = partition(arr, p, r)
    k = q - p + 1
    if i == k:
        return arr[q]
    elif i < k:
        return select(arr, p, q - 1, i)
    else:
        return select(arr, q + 1, r, i - k)


def Quicksort(arr, p, r):
    while(p < r):
        q = partition(arr, p, r)
        Quicksort(arr, p, q - 1)
        p = q + 1


arr = [5, 4, 2, 7, 9, 6, 8]
print(arr)
print(select(arr, 0, len(arr) - 1, 5))
