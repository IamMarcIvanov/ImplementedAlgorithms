import random
import time

def bubble_sort(A):
    # In place, stable(pls check) sorting of A using bubble sort with early stopping

    n = len(A)
    for i in range(n):
        swaps = 0
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swaps += 1
                A[j], A[j+1] = A[j+1], A[j]

        if swaps == 0:
            break

    return A

def insertion_sort(A):
    # In place

    n = len(A)
    for i in range(1,n):
        temp = A[i]
        j = i-1
        while j >= 0 and A[j] > temp:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = temp

    return A

def selection_sort(A):

    n = len(A)
    for i in range(n-1):

        min_element = A[n-1]
        min_ind = n-1

        for j in range(i,n):
            if A[j] < min_element:
                min_element = A[j]
                min_ind = j

        A[i], A[min_ind] = A[min_ind], A[i]

    return A


list_to_sort=random.choices(range(1,int(1e5)),k=1000)
print("unsorted\n",list_to_sort)
start_time = time.time()
# bubble_sort(list_to_sort)
# insertion_sort(list_to_sort)
selection_sort(list_to_sort)
end_time = time.time()
print("sorted\n",list_to_sort)
print("Total time taken =",end_time-start_time)

# Apparently selection sort is the best, then insertion sort and then bubble sort
