"""
Unit tests for the DoublyLinkedList implementation.
"""

import unittest
from doubly_linked_list import DoublyLinkedList, Node


class TestNode(unittest.TestCase):
    """Test cases for the Node class."""
    
    def test_node_creation(self):
        """Test creating a new node."""
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)


class TestDoublyLinkedList(unittest.TestCase):
    """Test cases for the DoublyLinkedList class."""
    
    def setUp(self):
        """Set up a new doubly linked list before each test."""
        self.dll = DoublyLinkedList()
    
    def test_initialization(self):
        """Test initializing an empty list."""
        self.assertTrue(self.dll.is_empty())
        self.assertEqual(len(self.dll), 0)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
    
    def test_append(self):
        """Test appending elements to the list."""
        self.dll.append(1)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 1)
        
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(len(self.dll), 3)
        self.assertEqual(self.dll.to_list(), [1, 2, 3])
        self.assertEqual(self.dll.tail.data, 3)
    
    def test_prepend(self):
        """Test prepending elements to the list."""
        self.dll.prepend(1)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.head.data, 1)
        
        self.dll.prepend(2)
        self.dll.prepend(3)
        self.assertEqual(len(self.dll), 3)
        self.assertEqual(self.dll.to_list(), [3, 2, 1])
        self.assertEqual(self.dll.head.data, 3)
    
    def test_insert_at(self):
        """Test inserting at specific indices."""
        self.dll.append(1)
        self.dll.append(3)
        self.dll.insert_at(1, 2)
        self.assertEqual(self.dll.to_list(), [1, 2, 3])
        
        self.dll.insert_at(0, 0)
        self.assertEqual(self.dll.to_list(), [0, 1, 2, 3])
        
        self.dll.insert_at(4, 4)
        self.assertEqual(self.dll.to_list(), [0, 1, 2, 3, 4])
    
    def test_insert_at_invalid_index(self):
        """Test inserting at invalid indices."""
        with self.assertRaises(IndexError):
            self.dll.insert_at(-1, 1)
        
        with self.assertRaises(IndexError):
            self.dll.insert_at(1, 1)
    
    def test_delete_first(self):
        """Test deleting the first element."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        data = self.dll.delete_first()
        self.assertEqual(data, 1)
        self.assertEqual(self.dll.to_list(), [2, 3])
        self.assertEqual(len(self.dll), 2)
    
    def test_delete_first_empty_list(self):
        """Test deleting from an empty list."""
        with self.assertRaises(IndexError):
            self.dll.delete_first()
    
    def test_delete_last(self):
        """Test deleting the last element."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        data = self.dll.delete_last()
        self.assertEqual(data, 3)
        self.assertEqual(self.dll.to_list(), [1, 2])
        self.assertEqual(len(self.dll), 2)
    
    def test_delete_at(self):
        """Test deleting at specific indices."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.append(4)
        
        data = self.dll.delete_at(2)
        self.assertEqual(data, 3)
        self.assertEqual(self.dll.to_list(), [1, 2, 4])
        
        data = self.dll.delete_at(0)
        self.assertEqual(data, 1)
        self.assertEqual(self.dll.to_list(), [2, 4])
    
    def test_delete_at_invalid_index(self):
        """Test deleting at invalid indices."""
        self.dll.append(1)
        
        with self.assertRaises(IndexError):
            self.dll.delete_at(-1)
        
        with self.assertRaises(IndexError):
            self.dll.delete_at(1)
    
    def test_delete_value(self):
        """Test deleting by value."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.append(2)
        
        result = self.dll.delete_value(2)
        self.assertTrue(result)
        self.assertEqual(self.dll.to_list(), [1, 3, 2])
        
        result = self.dll.delete_value(5)
        self.assertFalse(result)
        self.assertEqual(self.dll.to_list(), [1, 3, 2])
    
    def test_find(self):
        """Test finding elements by value."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        self.assertEqual(self.dll.find(2), 1)
        self.assertEqual(self.dll.find(1), 0)
        self.assertEqual(self.dll.find(3), 2)
        self.assertEqual(self.dll.find(5), -1)
    
    def test_get_at(self):
        """Test getting elements at specific indices."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        
        self.assertEqual(self.dll.get_at(0), 10)
        self.assertEqual(self.dll.get_at(1), 20)
        self.assertEqual(self.dll.get_at(2), 30)
    
    def test_get_at_invalid_index(self):
        """Test getting at invalid indices."""
        self.dll.append(1)
        
        with self.assertRaises(IndexError):
            self.dll.get_at(-1)
        
        with self.assertRaises(IndexError):
            self.dll.get_at(1)
    
    def test_reverse(self):
        """Test reversing the list."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.append(4)
        
        self.dll.reverse()
        self.assertEqual(self.dll.to_list(), [4, 3, 2, 1])
        self.assertEqual(self.dll.head.data, 4)
        self.assertEqual(self.dll.tail.data, 1)
        
        # Test reverse on empty list
        empty_dll = DoublyLinkedList()
        empty_dll.reverse()
        self.assertTrue(empty_dll.is_empty())
        
        # Test reverse on single element
        single_dll = DoublyLinkedList()
        single_dll.append(1)
        single_dll.reverse()
        self.assertEqual(single_dll.to_list(), [1])
    
    def test_to_list_reverse(self):
        """Test converting to list in reverse order."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        self.assertEqual(self.dll.to_list_reverse(), [3, 2, 1])
    
    def test_clear(self):
        """Test clearing the list."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        self.dll.clear()
        self.assertTrue(self.dll.is_empty())
        self.assertEqual(len(self.dll), 0)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
    
    def test_iterator(self):
        """Test iterating over the list."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        values = [value for value in self.dll]
        self.assertEqual(values, [1, 2, 3])
    
    def test_string_representation(self):
        """Test string representation."""
        self.assertEqual(str(self.dll), "DoublyLinkedList([])")
        
        self.dll.append(1)
        self.dll.append(2)
        self.assertEqual(str(self.dll), "DoublyLinkedList([1, 2])")
    
    def test_prev_pointers(self):
        """Test that previous pointers are correctly set."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        # Check forward traversal
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.head.next.next.data, 3)
        
        # Check backward traversal
        self.assertEqual(self.dll.tail.data, 3)
        self.assertEqual(self.dll.tail.prev.data, 2)
        self.assertEqual(self.dll.tail.prev.prev.data, 1)
        
        # Check that first node's prev is None
        self.assertIsNone(self.dll.head.prev)
        # Check that last node's next is None
        self.assertIsNone(self.dll.tail.next)


if __name__ == '__main__':
    unittest.main()
