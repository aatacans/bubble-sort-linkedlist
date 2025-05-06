# sorting_algorithms.py

from linked_list import LinkedList

def bubble_sort(collection):
    # Listeyse:
    if isinstance(collection, list):
        n = len(collection)
        for i in range(n):
            for j in range(0, n - i - 1):
                if collection[j] > collection[j + 1]:
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
        return collection

    # LinkedList’se:
    elif isinstance(collection, LinkedList):
        swapped = True
        while swapped:
            swapped = False
            node = collection.head
            while node and node.next:
                if node.data > node.next.data:
                    node.data, node.next.data = node.next.data, node.data
                    swapped = True
                node = node.next
        return collection

    else:
        raise TypeError("bubble_sort yalnızca list ve LinkedList destekler")
