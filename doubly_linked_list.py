"""
Doubly Linked List Implementation in Python

This module provides a complete implementation of a doubly linked list
data structure with standard operations.
"""


class Node:
    """
    A node in a doubly linked list.
    
    Attributes:
        data: The value stored in the node
        next: Reference to the next node in the list
        prev: Reference to the previous node in the list
    """
    
    def __init__(self, data):
        """
        Initialize a new node.
        
        Args:
            data: The value to store in the node
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    A doubly linked list data structure.
    
    Supports insertion, deletion, and traversal in both directions.
    
    Attributes:
        head: Reference to the first node in the list
        tail: Reference to the last node in the list
        size: The number of nodes in the list
    """
    
    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        """
        Check if the list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise
        """
        return self.head is None
    
    def __len__(self):
        """
        Get the number of nodes in the list.
        
        Returns:
            int: The number of nodes
        """
        return self.size
    
    def append(self, data):
        """
        Add a new node with the given data to the end of the list.
        
        Args:
            data: The value to add to the list
        """
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
        """
        Add a new node with the given data to the beginning of the list.
        
        Args:
            data: The value to add to the list
        """
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
        """
        Insert a new node with the given data at the specified index.
        
        Args:
            index: The position where the new node should be inserted (0-based)
            data: The value to add to the list
            
        Raises:
            IndexError: If the index is out of range
        """
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
        """
        Delete the node at the specified index.
        
        Args:
            index: The position of the node to delete (0-based)
            
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If the index is out of range or the list is empty
        """
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
        """
        Delete the first node in the list.
        
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If the list is empty
        """
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
        """
        Delete the last node in the list.
        
        Returns:
            The data from the deleted node
            
        Raises:
            IndexError: If the list is empty
        """
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
        """
        Delete the first node containing the specified value.
        
        Args:
            value: The value to search for and delete
            
        Returns:
            bool: True if a node was deleted, False if the value was not found
        """
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
        """
        Find the index of the first node containing the specified value.
        
        Args:
            value: The value to search for
            
        Returns:
            int: The index of the first occurrence, or -1 if not found
        """
        current = self.head
        index = 0
        
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get_at(self, index):
        """
        Get the data at the specified index.
        
        Args:
            index: The position of the node (0-based)
            
        Returns:
            The data at the specified index
            
        Raises:
            IndexError: If the index is out of range
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    def reverse(self):
        """
        Reverse the doubly linked list in place.
        """
        if self.is_empty() or self.size == 1:
            return
        
        current = self.head
        self.head, self.tail = self.tail, self.head
        
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
    
    def to_list(self):
        """
        Convert the doubly linked list to a Python list.
        
        Returns:
            list: A list containing all the values in the doubly linked list
        """
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    
    def to_list_reverse(self):
        """
        Convert the doubly linked list to a Python list in reverse order.
        
        Returns:
            list: A list containing all the values in reverse order
        """
        result = []
        current = self.tail
        
        while current:
            result.append(current.data)
            current = current.prev
        
        return result
    
    def clear(self):
        """Remove all nodes from the list."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        """
        String representation of the doubly linked list.
        
        Returns:
            str: A string showing the list structure
        """
        if self.is_empty():
            return "DoublyLinkedList([])"
        
        values = self.to_list()
        return f"DoublyLinkedList({values})"
    
    def __repr__(self):
        """
        Detailed representation of the doubly linked list.
        
        Returns:
            str: A string showing the list structure
        """
        return self.__str__()
    
    def __iter__(self):
        """
        Make the doubly linked list iterable.
        
        Yields:
            The data from each node in forward order
        """
        current = self.head
        while current:
            yield current.data
            current = current.next
