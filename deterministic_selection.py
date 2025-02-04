import math

def partition(arr, low, high, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def select(arr, low, high, k):
    if low == high:
        return arr[low]

    medians = [sorted(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(low, high+1, 5)]
    median_of_medians = select(medians, 0, len(medians)-1, len(medians)//2) if len(medians) > 1 else medians[0]

    pivot_index = arr.index(median_of_medians)
    pivot_index = partition(arr, low, high, pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return select(arr, low, pivot_index-1, k)
    else:
        return select(arr, pivot_index+1, high, k)

def deterministic_select(arr, k):
    return select(arr, 0, len(arr) - 1, k)
