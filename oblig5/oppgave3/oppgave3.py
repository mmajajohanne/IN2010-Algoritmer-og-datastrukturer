import sys # for å jobbe med kommandolinjeargumenter
import os # for å jobbe med filer og filnavn

# quicksort-funksjonen
def quicksort(arr):
    if len(arr) <= 1:  # hvis listen er tom eller har ett element, er den allerede sortert
        return arr
    
    pivot = arr[len(arr) // 2]  # velger et pivot-element (her: midten av listen)
    
    left = []    # liste for elementer som er mindre enn pivot
    middle = []  # liste for elementer som er lik pivot
    right = []   # liste for elementer som er større enn pivot

    # deler opp elementene i left, middle og right
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    # rekursivt kall for venstre og høyre del
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    # henter input-filnavn fra kommandolinjeargument
    if len(sys.argv) != 2:
        print("Bruk: python programmet.py <input_fil>") 
        sys.exit(1)

    input_filename = sys.argv[1] 
    
    # fjerner filendingen (for eksempel .txt) og legg til _out.txt for output-filen
    base_filename = os.path.splitext(input_filename)[0] 
    output_filename = base_filename + "_out.txt"

    # leser tallene fra input-filen
    with open(input_filename, 'r') as f:
        numbers = list(map(int, f.read().split())) # konverterer tallene til en liste av heltall

    # sorterer tallene ved hjelp av quicksort
    sorted_numbers = quicksort(numbers)

    # skriver de sorterte tallene til output-filen
    with open(output_filename, 'w') as f:
        for num in sorted_numbers:
            f.write(f"{num}\n")