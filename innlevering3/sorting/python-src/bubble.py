def sort(A):
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A.swap(j, j + 1)  # bruker swap-metoden, som teller bytter automatisk
                swapped = True
        if not swapped:
            break  # hvis ingen bytter skjedde i denne runden, er arrayet sortert
    return A