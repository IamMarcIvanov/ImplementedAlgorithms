def radix_sort(A):
  """assumes that the length of the elements is the same"""
    d = len(str(A[0]))
    for i in range(1, d + 1):
        A.sort(key=lambda x: str(x)[-i])
    return A
