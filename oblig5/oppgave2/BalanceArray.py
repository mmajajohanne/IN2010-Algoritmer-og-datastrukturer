def print_balanced_bst(arr):
    def inorder_print(arr, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        # print midt element (roten av dette subtreet)
        print(arr[mid])
        # rekursivt skriv ut venstre og høyre subtrær
        inorder_print(arr, start, mid - 1)
        inorder_print(arr, mid + 1, end)

    inorder_print(arr, 0, len(arr) - 1)


# eksempel bruk
if __name__ == "__main__":
    # lese input fra stdin:
    arr = list(map(int, input().split()))
    print_balanced_bst(arr)
