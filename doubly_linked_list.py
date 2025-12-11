class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self.size += 1

    def delete_at(self, index):
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list")
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.delete_first()
        if index == self.size - 1:
            return self.delete_last()
        current = self.head
        for _ in range(index):
            current = current.next
        data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return data

    def delete_first(self):
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list")
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data

    def delete_last(self):
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list")
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data

    def delete_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.delete_first()
                    self.size -= 1
                elif current == self.tail:
                    self.delete_last()
                    self.size -= 1
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                return True
            current = current.next
        return False

    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def get_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def reverse(self):
        if self.is_empty() or self.size == 1:
            return
        current = self.head
        self.head, self.tail = self.tail, self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def to_list_reverse(self):
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.is_empty():
            return "DoublyLinkedList([])"
        values = self.to_list()
        return f"DoublyLinkedList({values})"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next




