def heapify(arr, index, length_of_array):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    #print('heapify run')
    if left < length_of_array and arr[largest] < arr[left]:
        largest = left

    if right < length_of_array and arr[largest] < arr[right]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, largest, length_of_array)


def buildmaxheap(arr, length_of_array):

    for i in range(length_of_array - 1, -1, -1):
        heapify(arr, i, length_of_array)


def heapsort(arr):
    len1 = len(arr)
    for i in range(len1 - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        buildmaxheap(arr, i)


arr = [16, 4, 10, 14, 56, 76, 43, 13, 90, 23, 7, 9, 3, 2, 8, 1]
print(arr)
buildmaxheap(arr, len(arr))
print(arr)
heapsort(arr)
print(arr)
