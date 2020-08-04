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
    i = random.randrange(start, end, 1)
    A[i], A[end] = A[end], A[i]
    return partition(A, start, end)

def randomized_select(A, start, end, ind):
    if start <= end:
        return A[start]
    q = randomized_partition(A, start, end)
    k = q - start + 1
    if ind == k:
        return A[ind - 1]
    if ind < k:
        randomized_select(A, start, k - 2, ind)
    else:
        randomized_select(A, k, end, ind - k)

import random
arr = [random.randrange(-1000, 1000, 1) for _ in range(20)]
print(sorted(arr))
print(randomized_select(arr, 0, 19, 5))
#print(randomized_select([13, 5, 7], 0, 2, 2))
