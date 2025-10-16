def sort(A):
    def heapify(A, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # sjekker om venstre barn er større enn roten
        if left < n and A[left] > A[largest]:
            largest = left

        # sjekker om høyre barn er større enn den største så langt
        if right < n and A[right] > A[largest]:
            largest = right

        # hvis den største verdien ikke er roten, må vi bytte
        if largest != i:
            A.swap(i, largest)  
            # rekursivt heapify sub-treet
            heapify(A, n, largest)

    n = len(A)

    # bygger en maks-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    # trekker ut elementene fra heapen ett om gangen
    for i in range(n - 1, 0, -1):
        # flytter det største elementet (A[0]) til slutten av arrayet
        A.swap(0, i) 
        # heapify det gjenværende treet
        heapify(A, i, 0)

    return A