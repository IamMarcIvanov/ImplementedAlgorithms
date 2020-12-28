import random
import time

def parent(x):
    return (x - 1) // 2

def left(x):
    return 2 * (x + 1) - 1

def right(x):
    return 2 * (x + 1)

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest,heap_size)

def min_heapify(A, i, heap_size):
    if i < (heap_size / 2) - 1:
        swap = left(i) if A[left(i)] < A[right(i)] else right(i)
        if A[i] > A[swap]:
            A[i], A[swap] = A[swap], A[i]
            max_heapify(A, swap,heap_size)

def build_max_heap(A,heap_size):
    last_non_leaf_ind = (heap_size // 2) - 1
    for i in range(last_non_leaf_ind, -1, -1):
        max_heapify(A, i,heap_size)

def build_min_heap(A, heap_size):
    last_non_leaf_ind = (heap_size // 2) - 1
    for i in range(last_non_leaf_ind, -1, -1):
        min_heapify(A, i, heap_size)

def heapsort(A, heap_size, reverse=False):
    build_max_heap(A,heap_size)
    for i in range(heap_size - 1):
        A[0], A[heap_size - 1] = A[heap_size - 1], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)
        #print(A)
    if reverse:
        A.reverse()


list_to_sort=random.choices(range(1,int(1e5)),k=20000)
print("unsorted\n",list_to_sort)
start_time = time.time()
heapsort(list_to_sort,len(list_to_sort))
end_time = time.time()
print("sorted\n",list_to_sort)
print("Time taken =",end_time - start_time)