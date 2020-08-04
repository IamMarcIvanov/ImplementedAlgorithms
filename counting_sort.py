def min_max(X):
    n = len(X)
    small, big = X[0], X[0]
    if n == 1:
        return small, big
    elif n % 2 == 0:
        big = X[1]
    for i in range(2 - (n % 2), n - 1, 2):
        if X[i] < X[i + 1]:
            if X[i] < small:
                small = X[i]
            if X[i + 1] > big:
                big = X[i + 1]
        else:
            if small > X[i + 1]:
                small = X[i + 1]
            if big < X[i]:
                big = X[i]
    return small, big

A = list(map(int, input().split()))
sz = min_max(A)
B = [0] * (sz[1] - sz[0] + 1)
arr = [0] * len(A)
for val in A:
    B[val - sz[0]] += 1
for i in range(1, len(B)):
    B[i] += B[i - 1]
for val in A:
    arr[B[val - sz[0]] - 1] = val
    B[val - sz[0]] -= 1
print(arr)
