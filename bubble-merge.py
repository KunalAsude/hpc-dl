from multiprocessing import Pool
import time


def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def swap(pair):

    a, b = pair

    return (min(a, b), max(a, b))


def parallel_bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        pairs = []

        for j in range(0, n - 1, 2):

            pairs.append((arr[j], arr[j + 1]))

        with Pool() as pool:

            result = pool.map(swap, pairs)

        k = 0

        for j in range(0, n - 1, 2):

            arr[j], arr[j + 1] = result[k]

            k += 1

    return arr


def merge(left, right):

    result = []

    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    result += left[i:]

    result += right[j:]

    return result


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])

    right = merge_sort(arr[mid:])

    return merge(left, right)


def parallel_merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    with Pool(2) as pool:

        left, right = pool.map(
            merge_sort,
            [arr[:mid], arr[mid:]]
        )

    return merge(left, right)


if __name__ == "__main__":

    arr = [2, 5, 6, 4, 7, 3, 1]

    print("Original Array:", arr)

    start = time.time()

    bubble_sort(arr.copy())

    print("Sequential Bubble Sort Time:",
          time.time() - start)

    start = time.time()

    parallel_bubble_sort(arr.copy())

    print("Parallel Bubble Sort Time:",
          time.time() - start)

    start = time.time()

    merge_sort(arr.copy())

    print("Sequential Merge Sort Time:",
          time.time() - start)

    start = time.time()

    parallel_merge_sort(arr.copy())

    print("Parallel Merge Sort Time:",
          time.time() - start)