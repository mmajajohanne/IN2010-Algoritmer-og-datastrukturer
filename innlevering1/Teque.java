//kjører koden med kommandoer som disse:
//java Teque < inputs/input_10
//java Teque < inputs/input_10 | cmp - outputs/output_10

import java.util.Scanner;

class LinkedList {

    private class Node {
        int value;
        Node next;
        Node prev;

        Node(int value) {
            this.value = value;
            this.next = null;
            this.prev = null;
        }
    }

    Node head;
    Node tail;
    int size;

    LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    void push_back(int value) {
        Node newNode = new Node(value);
        if (tail == null) {
            head = tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }

    void push_front(int value) {
        Node newNode = new Node(value);
        if (head == null) {
            head = tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        size++;
    }

    void push_middle(int index, int value) {
        if (index <= 0) {
            push_front(value);
            return;
        }
        if (index >= size) {
            push_back(value);
            return;
        }
        Node newNode = new Node(value);
        Node current = head;
        for (int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        newNode.next = current.next;
        newNode.prev = current;
        if (current.next != null) {
            current.next.prev = newNode;
        }
        current.next = newNode;
        size++;
    }

    int get(int index) {
        Node current = head;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }
        return current.value;
    }
}

class TequeList {
    LinkedList data;

    TequeList() {
        this.data = new LinkedList();
    }

    void push_back(int x) {
        data.push_back(x);
    }

    void push_front(int x) {
        data.push_front(x);
    }

    void push_middle(int x) {
        int mid = data.size / 2;
        data.push_middle(mid, x);
    }

    int get(int i) {
        return data.get(i);
    }
}

public class Teque {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        TequeList teque = new TequeList();

        for (int i = 0; i < N; i++) {
            String[] operation = scanner.nextLine().split(" ");
            String command = operation[0];
            int value = Integer.parseInt(operation[1]);

            switch (command) {
                case "push_back":
                    teque.push_back(value);
                    break;
                case "push_front":
                    teque.push_front(value);
                    break;
                case "push_middle":
                    teque.push_middle(value);
                    break;
                case "get":
                    System.out.println(teque.get(value));
                    break;
            }
        }
        scanner.close();
    }
}