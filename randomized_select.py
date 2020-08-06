def partition(A, start, end, ind):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    if i + 1 == ind:
        print(A[i + 1])
    return i + 1

def randomized_partition(A, start, end, ind):
    import random
    if start == end:
        i = start
    else:
        i = random.randrange(start, end, 1)
    A[i], A[end] = A[end], A[i]
    return partition(A, start, end, ind)

def quicksort(A, start, end, ind):
    if start <= end:
        q = randomized_partition(A, start, end, ind)
        if q == ind:
            return A[q]
        if ind > q:
            quicksort(A, q + 1, end, ind)
        else:
            quicksort(A, start, q - 1, ind)

import random
arr = [random.randrange(-1000, 1000, 1) for _ in range(10)]
print(arr)
print(sorted(arr))
quicksort(arr, 0, 9, 4)
