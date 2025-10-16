"""
Kjører koden med kommandoer som disse:
    python3 AVL_set.py < inputs/eksempel_input
    python3 AVL_set.py < inputs/input_100 | cmp - outputs/output_100
"""
# definerer en node i treet. Hver node inneholder en verdi, en referanse til sitt venstre barn, høyre barn og høyden.
class Node:
    def __init__(self, x):
        self.value = x  # verdi i noden
        self.left = None  # referanse til venstre barn
        self.right = None  # referanse til høyre barn
        self.height = 1  # høyden på noden starter som 1

# definerer AVL-treet
class AVLTree:
    def __init__(self):
        self.root = None  # roten av treet
        self.size = 0  # for å holde styr på antall elementer i treet

    # funksjon for å sette inn en node i AVL-treet
    def insert(self, x):
        if not self.root:  # hvis treet er tomt, opprett en ny rot-node
            self.root = Node(x)
            self.size += 1 
        else:  # hvis ikke: sett inn noden rekursivt
            self.root = self._insert_recursive(self.root, x)

    # intern rekursiv funksjon for å sette inn en node
    def _insert_recursive(self, node, x):
        # 1. vanlig BST-innsetting
        if not node:  # hvis noden er None, opprett en ny node
            self.size += 1 
            return Node(x)
        
        # rekursivt sett inn i venstre eller høyre under-tre basert på verdien
        if x < node.value:  # hvis verdien er mindre enn nodens verdi, gå til venstre under-tre
            node.left = self._insert_recursive(node.left, x)
        elif x > node.value:  # hvis verdien er større, gå til høyre under-tre
            node.right = self._insert_recursive(node.right, x)
        else:  # hvis verdien allerede finnes, gjør ingenting (ingen duplikater tillatt)
            return node

        # 2. oppdater høyden på forelder-noden
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # 3. finne balansefaktoren for å sjekke om treet er blitt ubalansert
        balance = self._get_balance(node)

        # 4. hvis ubalansert, er det 4 mulige tilfeller:
        # høyre rotasjon
        if balance > 1 and x < node.left.value:
            return self._rotate_right(node)

        # venstre rotasjon
        if balance < -1 and x > node.right.value:
            return self._rotate_left(node)

        # venstre rotasjon etterfulgt av høyre rotasjon
        if balance > 1 and x > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # høyre rotasjon etterfulgt av venstre rotasjon
        if balance < -1 and x < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node  # returnerer (potensielt rotert) node

    # funksjon for å fjerne en node fra treet
    def remove(self, x):
        self.root = self._remove_recursive(self.root, x)

    # intern rekursiv funksjon for å fjerne en node
    def _remove_recursive(self, node, x):
        if not node: 
            return node

        if x < node.value:  
            node.left = self._remove_recursive(node.left, x)
        elif x > node.value: 
            node.right = self._remove_recursive(node.right, x)
        else: 
            if not node.left: 
                self.size -= 1
                return node.right
            elif not node.right: 
                self.size -= 1
                return node.left

            temp = self._min_value_node(node.right)
            node.value = temp.value  
            node.right = self._remove_recursive(node.right, temp.value) 

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node 

    # hjelpefunksjon for å finne noden med minst verdi i et under-tre
    def _min_value_node(self, node):
        current = node

        while current.left:
            current = current.left
        return current

    # hjelpefunksjon for å få høyden til en node
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # hjelpefunksjon for å få balansefaktoren til en node
    def _get_balance(self, node):
        if not node: 
            return 0
        return self._get_height(node.left) - self._get_height(node.right)  # forskjell i høyder mellom venstre og høyre under-tre

    # høyre rotasjon funksjon
    def _rotate_right(self, y):
        x = y.left  # x blir den nye roten
        T2 = x.right  # T2 er x sitt høyre under-tre
        # utfør rotasjonen
        x.right = y
        y.left = T2
        # oppdater høydene til de berørte nodene
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    # venstre rotasjon funksjon
    def _rotate_left(self, x):
        y = x.right  # y blir den nye roten
        T2 = y.left  # T2 er y sitt venstre under-tre

        y.left = x
        x.right = T2

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    # funksjon for å få størrelsen på treet (antall elementer)
    def get_size(self):
        return self.size

    # funksjon for å sjekke om en verdi finnes i treet
    def contains(self, x):
        return self._contains_recursive(self.root, x)

    # rekursiv funksjon for å sjekke om en verdi finnes
    def _contains_recursive(self, node, x):
        if not node: 
            return False
        if x == node.value: 
            return True
        elif x < node.value: 
            return self._contains_recursive(node.left, x)
        else: 
            return self._contains_recursive(node.right, x)


def main():
    avl_tree = AVLTree()
    N = int(input()) 

    for _ in range(N):
        command = input().split()  
        if command[0] == "insert":
            avl_tree.insert(int(command[1]))
        elif command[0] == "contains":
            print("true" if avl_tree.contains(int(command[1])) else "false")
        elif command[0] == "remove":
            avl_tree.remove(int(command[1]))
        elif command[0] == "size":
            print(avl_tree.get_size())

if __name__ == "__main__":
    main()