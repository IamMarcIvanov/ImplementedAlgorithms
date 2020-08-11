import random

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

    i = random.randrange(start, end+1, 1)
    A[i], A[end] = A[end], A[i]
    return partition(A, start, end)

def quicksort(A, start, end):
    if start < end:
        q = randomized_partition(A, start, end)
        quicksort(A, start, q - 1)
        quicksort(A, q + 1, end)


list_to_sort=random.choices(range(1,int(1e5)),k=25)
print("unsorted\n",list_to_sort)
quicksort(list_to_sort,0,len(list_to_sort)-1)
print("sorted\n",list_to_sort)



