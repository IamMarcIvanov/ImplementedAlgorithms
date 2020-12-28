import time
import random
import sys

def merge_sort(A, start, end):
    global tempA
    
    if start + 1 >= end:
        return
    
    mid = (start + end)//2
    # print("start=",start, "end=",end,"mid=",mid)
    
    # Recursive step
    merge_sort(A, start, mid)
    merge_sort(A, mid, end)
    
    i = start
    j = mid
    temp_ind = start
    while i < mid and j < end:
        # print("i=",i,"j=",j)
        if A[i] > A[j]:
            tempA[temp_ind] = A[j]
            j += 1
        else:
            tempA[temp_ind] = A[i]
            i += 1
        
        temp_ind += 1
    
    while i < mid:
        # print("temp_ind",temp_ind)
        tempA[temp_ind] = A[i]
        temp_ind += 1
        i += 1
        
    while j < end:
        tempA[temp_ind] = A[j]        
        temp_ind += 1
        j += 1

    for c in range(start, end):
        A[c] = tempA[c]


list_to_sort=random.choices(range(1,int(1e5)),k=30000)
# Providing extra memory for merge sort globally (No local allocation/deallocation required)
tempA = [0]*len(list_to_sort)
# print(tempA)
print("unsorted\n",list_to_sort)
start_time = time.time()
merge_sort(list_to_sort,0,len(list_to_sort))
end_time = time.time()
print("sorted\n",list_to_sort)
print("Total time taken =",end_time-start_time)