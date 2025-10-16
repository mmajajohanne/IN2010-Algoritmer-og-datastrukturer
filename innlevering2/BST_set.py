"""
Kjører koden med kommandoer som disse:
    python3 BST_set.py < inputs/eksempel_input
    python3 BST_set.py < inputs/input_100 | cmp - outputs/output_100
"""
class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.value = x

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0  # for å holde styr på antall elementer

    # sett inn en node i treet
    def insert(self, x):
        if not self.root: # treet er tomt
            self.root = Node(x)
            self.size += 1
        else:
            self._insert_recursive(self.root, x)
    
    def _insert_recursive(self, current_node, x): # hjelpemetode for å sette inn en node
        #hvis verdien x er mindre enn verdien i den nåværende noden, så skal man sette x inn i venstre del av treet
        if x < current_node.value: 
            if current_node.left:   #hvis venstre barn finnes, kaller man _insert_recursive på venstre barn,
                self._insert_recursive(current_node.left, x)
            else:  #hvis venstre barn ikke finnes, setter man inn den nye noden med verdien x som venstre barn til current 
                current_node.left = Node(x)
                self.size += 1
        # samme men for høyre del av treet dersom x er større enn verdien i den nåværende noden
        elif x > current_node.value:  
            if current_node.right:
                self._insert_recursive(current_node.right, x)
            else:
                current_node.right = Node(x)
                self.size += 1

    # sjekke om en gitt node er med i treet (rekursivt)
    def contains(self, x):
        return self._contains_recursive(self.root, x)

    def _contains_recursive(self, current_node, x): # hjelpemetode for å sjekke om en node er med i treet
        if not current_node: #sjekker om noden eksisterer
            return False
        if x == current_node.value: #sjekker om veriden til noden er lik x
            return True
        elif x < current_node.value: #hvis x er mindre enn verdien til noden, sjekk til venstre
            return self._contains_recursive(current_node.left, x)
        else: #ellers er x større enn verdien til noden, sjekk til høyre
            return self._contains_recursive(current_node.right, x)

    # fjerne node fra treet (rekursivt)
    def remove(self, x):
        self.root = self._remove_recursive(self.root, x)

    def _remove_recursive(self, current_node, x):
        if not current_node: #sjekker om noden eksisterer
            return current_node
        if x < current_node.value: #hvis x er mindre enn verdien til noden, sjekk til venstre
            current_node.left = self._remove_recursive(current_node.left, x)
        elif x > current_node.value: #ellers er x større enn verdien til noden, sjekk til høyre
            current_node.right = self._remove_recursive(current_node.right, x)
        else: # når noden som skal fjernes er funnet
            if not current_node.left: # hvis noden har ingen eller bare ett barn (høyre barn)
                self.size -= 1 
                return current_node.right # bytt ut noden med høyre barn (kan være None)
            elif not current_node.right: # hvis noden har bare venstre barn
                self.size -= 1
                return current_node.left # bytt ut noden med venstre barn
            # hvis noden har to barn (venstre og høyre)
            temp = self._min_value_node(current_node.right) # finn minimumsverdi i høyre undertre (hjelpemetode)
            current_node.value = temp.value # bytt nodens verdi med denne minimumsverdien
            current_node.right = self._remove_recursive(current_node.right, temp.value) # fjern den "gamle" minste noden
        return current_node

    # hjelpemetode for å finne noden med minst verdi i et tre (noden lengst til venstre)
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # returnerer størrelsen på treet
    def size(self):
        return self.size
    

def main():
    bst = BinarySearchTree()
    N = int(input())  # leser antall operasjoner

    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            bst.insert(int(command[1]))
        elif command[0] == "contains":
            print("true" if bst.contains(int(command[1])) else "false")
        elif command[0] == "remove":
            bst.remove(int(command[1]))
        elif command[0] == "size":
            print(bst.size)

if __name__ == "__main__":
    main()