# linked_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        """Listenin sonuna ekler."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def __iter__(self):
        """LinkedList’i iterable yapar."""
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next
