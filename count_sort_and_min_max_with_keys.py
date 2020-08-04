def min_max(X):
    n = len(X)
    small, big = X[0][1], X[0][1]
    if n == 1:
        return small, big
    elif n % 2 == 0:
        if X[1][1] < X[0][1]:
            small = X[1][1]
        else:
            big = X[1][1] 
    for i in range(2 - (n % 2), n - 1, 2):
        if X[i][1] < X[i + 1][1]:
            if X[i][1] < small:
                small = X[i][1]
            if X[i + 1][1] > big:
                big = X[i + 1][1]
        else:
            if X[i + 1][1] < small:
                small = X[i + 1][1]
            if X[i][1] > big:
                big = X[i][1]
    return small, big

def count_sort(A): 
    sz = min_max(A)
    print(sz)
    B = [0] * (sz[1] - sz[0] + 1)
    arr = [0] * len(A)
    for val in A:
        B[val[1] - sz[0]] += 1
    for i in range(1, len(B)):
        B[i] += B[i - 1]
    for val in A:
        arr[B[val[1] - sz[0]] - 1] = val
        B[val[1] - sz[0]] -= 1
    return arr
