import heapq

def print_balanced_bst(arr):
    # prioritetskøen inneholder tupler som beskriver områder (negativ lengde, start, slutt)
    # ved å bruke negativ lengde, sørger man for at de største områdene behandles først (maks-heap oppførsel)
    queue = []
    
    # legger hele området i køen som det første området
    # bruker -len(arr) for å sikre at hele området prioriteres først
    heapq.heappush(queue, (-len(arr), 0, len(arr) - 1))

    while queue:
        # henter ut det største (mest negative) området fra køen
        # dette vil alltid gi det største gjenværende området i arrayet
        _, start, end = heapq.heappop(queue)

        # hvis start > end, betyr det at det er et tomt område, så fortsetter til neste iterasjon
        if start > end:
            continue

        # finner midtpunktet for området ved hjelp av indeksene start og end
        mid = (start + end) // 2

        # printer midtpunktet, dette blir roten i subtreet
        print(arr[mid])

        # legger venstre subområde (fra start til mid - 1) tilbake i køen
        # prioriteten er størrelsen på området (mid - start), gjort negativ for maks-heap
        heapq.heappush(queue, (-(mid - start), start, mid - 1))

        # legger høyre subområde (fra mid + 1 til end) tilbake i køen
        # prioriteten er størrelsen på området (end - mid), gjort negativ for maks-heap
        heapq.heappush(queue, (-(end - mid), mid + 1, end))


if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6,7,8,9,10]
    #list(map(int, input().split()))
    print_balanced_bst(arr)