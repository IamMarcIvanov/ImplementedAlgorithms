def partition(A, start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1

def randomized_partition(A, start, end):
    import random
    i = random.randrange(p, q, 1)
    A[i], A[end] = A[end], A[i]
    return partition(A, start, end)

def quicksort(A, start, end):
    if start < end:
        q = randomized_partition(A, start, end)
        quicksort(A, start, q - 1)
        quicksort(A, q + 1, end)


