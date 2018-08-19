def Quicksort(arr, p, r):
    if(p < r):
        q = Hoare_partition(arr, p, r)
        Quicksort(arr, p, q - 1)
        Quicksort(arr, q + 1, r)
#         print(arr)


''' right most element as pivot'''
# def partition(arr, p, r):
#     x = arr[r]
#     i = p - 1
#     for j in range(p, r):
#         if(arr[j] < x):
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[r] = arr[r], arr[i + 1]
#     return i + 1

'''' left most element as 
pivot'''


def partition(arr, p, r):
    x = arr[p]
    i = p
    for j in range(p + 1, r + 1):
        if(arr[j] > x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[p] = arr[p], arr[i]
    return i


'''' Middle element as 
pivot'''


# def partition(arr, p, r):
#     x = p + ((r - p) // 2)
#     i, j = p, r
#     while(i <= j):
#         while(arr[i] < arr[x]):
#             i += 1
#         while(arr[j] > arr[x]):
#             j -= 1
#
#         if(i <= j):
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1
#
#     return x
def Hoare_partition(arr, p, r):
    x = arr[p]
    i = p - 1
    j = r + 1
    while(True):
        while(True):
            j -= 1
            if(arr[j] <= x):
                break
        while(True):
            i += 1
            if(arr[i] >= x):
                break
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return i


arr = [5, 4, 2, 7, 9, 6, 8]
print(arr)
Quicksort(arr, 0, len(arr) - 1)

print(arr)
