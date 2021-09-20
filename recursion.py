def recursionMultiple(m,n):
    if n == 0:
        return m
    else:
        return m + recursionMultiple(m,n-1)


def factorial(n):
    if n == 0 or n== 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(4))
print(recursionMultiple(4, 3))

