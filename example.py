"""
Example usage of the DoublyLinkedList class.

This module demonstrates various operations that can be performed
on a doubly linked list.
"""

from doubly_linked_list import DoublyLinkedList


def main():
    """Demonstrate doubly linked list operations."""
    
    print("=" * 50)
    print("Doubly Linked List - Example Usage")
    print("=" * 50)
    
    # Create a new doubly linked list
    dll = DoublyLinkedList()
    print("\n1. Created an empty doubly linked list")
    print(f"   List: {dll}")
    print(f"   Is empty: {dll.is_empty()}")
    print(f"   Size: {len(dll)}")
    
    # Append elements
    print("\n2. Appending elements: 10, 20, 30, 88")
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(88)
    print(f"   List: {dll}")
    print(f"   Size: {len(dll)}")
    
    # Prepend elements
    print("\n3. Prepending element: 5")
    dll.prepend(5)
    print(f"   List: {dll}")
    
    # Insert at specific position
    print("\n4. Inserting 15 at index 2")
    dll.insert_at(2, 15)
    print(f"   List: {dll}")
    
    # Access elements
    print("\n5. Accessing elements by index")
    print(f"   Element at index 0: {dll.get_at(0)}")
    print(f"   Element at index 2: {dll.get_at(2)}")
    print(f"   Element at index 4: {dll.get_at(4)}")
    
    # Find elements
    print("\n6. Finding elements by value")
    print(f"   Index of value 15: {dll.find(15)}")
    print(f"   Index of value 30: {dll.find(30)}")
    print(f"   Index of value 100: {dll.find(100)}")
    
    # Iterate over the list
    print("\n7. Iterating over the list")
    print("   Values: ", end="")
    for value in dll:
        print(value, end=" ")
    print()
    
    # Traverse in reverse
    print("\n8. Traversing in reverse order")
    print(f"   Reverse list: {dll.to_list_reverse()}")
    
    # Delete operations
    print("\n9. Deleting first element")
    deleted = dll.delete_first()
    print(f"   Deleted: {deleted}")
    print(f"   List: {dll}")
    print(f"   Size: {len(dll)}")

    
    print("\n10. Deleting last element")
    deleted = dll.delete_last()
    print(f"   Deleted: {deleted}")
    print(f"   List: {dll}")
    print(f"   Size: {len(dll)}")
    
    print("\n11. Deleting element at index 1")
    deleted = dll.delete_at(1)
    print(f"   Deleted: {deleted}")
    print(f"   List: {dll}")
    print(f"   Size: {len(dll)}")


    print("\n12. Deleting element by value (30)")
    success = dll.delete_value(30)
    print(f"   Deleted successfully: {success}")
    print(f"   List: {dll}")
    print(f"   Size: {len(dll)}")

    # Reverse the list
    print("\n13. Reversing the list")
    dll.append(25)
    dll.append(35)
    dll.append(45)
    print(f"   Before reverse: {dll}")
    dll.reverse()
    print(f"   After reverse: {dll}")
    
    # Convert to Python list
    print("\n14. Converting to Python list")
    py_list = dll.to_list()
    print(f"   Python list: {py_list}")
    
    # Clear the list
    print("\n15. Clearing the list")
    dll.clear()
    print(f"   List after clear: {dll}")
    print(f"   Is empty: {dll.is_empty()}")
    
    # Working with different data types
    print("\n16. Working with strings")
    string_dll = DoublyLinkedList()
    string_dll.append("apple")
    string_dll.append("banana")
    string_dll.append("cherry")
    string_dll.prepend("orange")
    print(f"   String list: {string_dll}")
    
    print("\n17. Working with mixed types")
    mixed_dll = DoublyLinkedList()
    mixed_dll.append(1)
    mixed_dll.append("two")
    mixed_dll.append(3.0)
    mixed_dll.append([4, 5])
    mixed_dll.append({"key": "value"})
    print(f"   Mixed list: {mixed_dll}")
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
