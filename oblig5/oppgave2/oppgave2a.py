def balanser_treet(arr):
    if not arr:
        return
    
    mid = len(arr) // 2
    print(arr[mid])  # Skriv ut medianen
    
    balanser_treet(arr[:mid])  # Venstre del
    balanser_treet(arr[mid+2:])  # HÃ¸yre del

# Les input og konverter til en liste med heltall
if __name__ == "__main__":
    arr = list(map(int, input().split()))  # Input: sortert array
    balanser_treet(arr)