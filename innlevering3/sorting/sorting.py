import sys

class Sorting:
    def __init__(self) -> None:
        pass

    def les_inn(self):
        input = sys.stdin.read
        data = input().splitlines()
        data = list(map(int, data))
        return data

    def skriv_ut(self, filnavn, data):
        with open(filnavn, "w") as f:
            for num in data:
                f.write(f"{num}\n")  # Skriv ut hver linje i samme format som input

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]  # lagrer det nåværende elementet i en midlertidig variabel
            j = i - 1  # sammenligninger med forrige element
            # flytter elementer som er større enn temp til én posisjon til høyre
            while j >= 0 and temp < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp  # sett inn temp på sin korrekte plass
        return arr

    def merge_sort(self, arr):
        # hvis listen har mer enn ett element, så del den og sorter delene
        if len(arr) > 1:
            # dele arrayet på midten
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            # rekursivt sortere begge halvdeler
            self.merge_sort(left_half)
            self.merge_sort(right_half)

            # merge de to halvdelene sammen
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                # hvis elementet i venstre halvdel er mindre, legg det til i arr
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                # hvis elementet i høyre halvdel er mindre eller lik, legg det til i arr
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # kopiere de resterende elementene fra venstre halvdel, hvis det er noen igjen
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
            # kopiere de resterende elementene fra høyre halvdel, hvis det er noen igjen
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr

    def heap_sort(self, arr):
        # hjelpefunksjon for å heapifisere et under-tre med rot ved indeks i
        def _heapify(arr, n, i):
            largest = i  # initialiser største som roten
            left = 2 * i + 1  # indeks til venstre barn
            right = 2 * i + 2  # indeks til høyre barn
            # sjekk om venstre barn finnes og er større enn roten
            if left < n and arr[i] < arr[left]:
                largest = left
            # sjekk om høyre barn finnes og er større enn den største så langt
            if right < n and arr[largest] < arr[right]:
                largest = right
            # endre rot hvis nødvendig
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # Bytt
                # rekursivt heapifiser det påvirkede under-treet
                _heapify(arr, n, largest)

        n = len(arr)
        # bygg en maks-heap
        for i in range(n // 2 - 1, -1, -1):
            _heapify(arr, n, i)

        # trekk ut elementene ett og ett fra heapen
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = (
                arr[0],
                arr[i],
            )  # bytt første element (størst) med det siste i arrayet
            _heapify(arr, i, 0)  # heapifiser roten for å opprettholde heap-egenskapen

        return arr  # returner den sorterte listen

    def bubble_sort(self, arr):
        n = len(arr)
        # gå gjennom alle elementene i listen
        for i in range(n):
            # siste i elementene er allerede sortert etter hver passering
            for j in range(0, n - i - 1):
                # sjekk om det gjeldende elementet er større enn neste element
                if arr[j] > arr[j + 1]:
                    # bytt elementene hvis de er i feil rekkefølge
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr  # returner den sorterte listen


def main():
    sort = Sorting()

    # les inn array fra stdin
    array = sort.les_inn()
    # definer terskel for liten/stor inputfil (her: 1000 elementer)
    terskel = 1000

    # Basenavn for outputfilene
    base_filnavn = "example"  # Du kan tilpasse dette om nødvendig

    # Hvis filen er liten, kjør alle algoritmer
    if len(array) <= terskel:
        # Kjør alle sorteringsalgoritmer
        insertion_sorted = sort.insertion_sort(array.copy())
        merge_sorted = sort.merge_sort(array.copy())
        heap_sorted = sort.heap_sort(array.copy())
        bubble_sorted = sort.bubble_sort(array.copy())

        # Skriv output til filer
        sort.skriv_ut(f"{base_filnavn}_insertion.out", insertion_sorted)
        sort.skriv_ut(f"{base_filnavn}_merge.out", merge_sorted)
        sort.skriv_ut(f"{base_filnavn}_heap.out", heap_sorted)
        sort.skriv_ut(f"{base_filnavn}_bubble.out", bubble_sorted)
    else:
        # For store filer, kjør bare de raskeste algoritmene (merge og heap)
        merge_sorted = sort.merge_sort(array.copy())
        heap_sorted = sort.heap_sort(array.copy())

        # Skriv output til filer
        sort.skriv_ut(f"{base_filnavn}_merge.out", merge_sorted)
        sort.skriv_ut(f"{base_filnavn}_heap.out", heap_sorted)


if __name__ == "__main__":
    main()
