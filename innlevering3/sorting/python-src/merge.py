def sort(A):
    # Do merge sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.
    def merge_sort(A, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort(A, left, mid)
            merge_sort(A, mid + 1, right)
            merge(A, left, mid, right)

    def merge(A, left, mid, right):
        # opprett midlertidige lister for venstre og høyre del
        L = A[left:mid + 1]
        R = A[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # kopierer de resterende elementene i L, hvis det er noen igjen
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        # kopierer de resterende elementene i R, hvis det er noen igjen
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

    merge_sort(A, 0, len(A) - 1)
    return A
