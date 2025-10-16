import heapq

def print_balanced_bst(arr):
    # Prioritetskøen inneholder tupler (negativ lengde, start, slutt)
    queue = []
    
    # Legger hele området i køen som første område
    heapq.heappush(queue, (-len(arr), 0, len(arr) - 1))

    while queue:
        _, start, end = heapq.heappop(queue)

        if start > end:
            continue

        # Finner midtpunktet for området ved hjelp av start og end
        mid = (start + end) // 2

        # Printer midtpunktet, roten i subtreet
        print(arr[mid])

        heapq.heappush(queue, (-(mid - start), start, mid - 1))  # Venstre subområde
        heapq.heappush(queue, (-(end - mid), mid + 1, end))  # Høyre subområde


if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6,7,8,9,10]
    print_balanced_bst(arr)
