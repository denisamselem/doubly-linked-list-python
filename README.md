# Doubly Linked List - Python Implementation

A complete implementation of a doubly linked list data structure in Python with comprehensive functionality, tests, and examples.

## Features

- **Full bidirectional traversal** - Navigate forward and backward through the list
- **Dynamic size management** - Automatic size tracking
- **Rich API** - Comprehensive set of operations
- **Type flexible** - Store any Python data type
- **Well tested** - Complete test suite included
- **Iterator support** - Use in for loops and list comprehensions

## Project Structure

```
.
├── doubly_linked_list.py      # Main implementation
├── test_doubly_linked_list.py # Unit tests
├── example.py                 # Usage examples
└── README.md                  # This file
```

## Installation

No external dependencies required. Just clone or download the repository:

```bash
git clone https://github.com/denisamselem/doubly-linked-list-python
cd doubly-linked-list-python
```

## Usage

### Basic Operations

```python
from doubly_linked_list import DoublyLinkedList

# Create a new doubly linked list
dll = DoublyLinkedList()

# Add elements
dll.append(10)      # Add to end
dll.prepend(5)      # Add to beginning
dll.insert_at(1, 7) # Insert at index

# Access elements
value = dll.get_at(0)           # Get by index
index = dll.find(10)            # Find by value
size = len(dll)                 # Get size
is_empty = dll.is_empty()       # Check if empty

# Delete elements
dll.delete_first()              # Remove first
dll.delete_last()               # Remove last
dll.delete_at(1)                # Remove at index
dll.delete_value(10)            # Remove by value

# Traverse
for value in dll:               # Forward iteration
    print(value)

reverse_list = dll.to_list_reverse()  # Backward traversal

# Other operations
dll.reverse()                   # Reverse the list in place
py_list = dll.to_list()         # Convert to Python list
dll.clear()                     # Remove all elements
```

### Running Examples

```bash
python example.py
```

This will demonstrate all the major operations of the doubly linked list.

## API Reference

### Node Class

```python
Node(data)
```

Represents a single node in the doubly linked list.

**Attributes:**
- `data` - The value stored in the node
- `next` - Reference to the next node
- `prev` - Reference to the previous node

### DoublyLinkedList Class

```python
DoublyLinkedList()
```

Main doubly linked list implementation.

**Methods:**

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `append(data)` | Add element to end | O(1) |
| `prepend(data)` | Add element to beginning | O(1) |
| `insert_at(index, data)` | Insert at specific index | O(n) |
| `delete_first()` | Remove first element | O(1) |
| `delete_last()` | Remove last element | O(1) |
| `delete_at(index)` | Remove at specific index | O(n) |
| `delete_value(value)` | Remove first occurrence of value | O(n) |
| `get_at(index)` | Get value at index | O(n) |
| `find(value)` | Find index of value | O(n) |
| `reverse()` | Reverse the list in place | O(n) |
| `to_list()` | Convert to Python list (forward) | O(n) |
| `to_list_reverse()` | Convert to Python list (backward) | O(n) |
| `clear()` | Remove all elements | O(1) |
| `is_empty()` | Check if list is empty | O(1) |
| `__len__()` | Get size of list | O(1) |
| `__iter__()` | Make list iterable | O(1) per item |



## Implementation Details

### Data Structure

The doubly linked list maintains:
- `head` - Reference to the first node
- `tail` - Reference to the last node
- `size` - Current number of nodes

Each node contains:
- `data` - The stored value
- `next` - Pointer to next node (or None)
- `prev` - Pointer to previous node (or None)

### Advantages

- **O(1) insertion/deletion** at both ends
- **Bidirectional traversal** - can move forward and backward
- **No memory waste** - only uses memory for stored elements
- **Dynamic size** - grows and shrinks as needed

### Disadvantages

- **Extra memory** - each node stores two pointers
- **O(n) access time** - must traverse to reach elements
- **More complex** - than singly linked lists

## Examples

### Example 1: Basic List Operations

```python
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print(dll)  # DoublyLinkedList([1, 2, 3])
```

### Example 2: Reverse Traversal

```python
dll = DoublyLinkedList()
for i in range(1, 4):
    dll.append(i)

# Forward
print(dll.to_list())          # [1, 2, 3]

# Backward
print(dll.to_list_reverse())  # [3, 2, 1]
```

### Example 3: Working with Strings

```python
dll = DoublyLinkedList()
dll.append("apple")
dll.append("banana")
dll.append("cherry")
print(dll)  # DoublyLinkedList(['apple', 'banana', 'cherry'])
```

### Example 4: List Reversal

```python
dll = DoublyLinkedList()
for i in [1, 2, 3, 4, 5]:
    dll.append(i)

print(dll.to_list())  # [1, 2, 3, 4, 5]
dll.reverse()
print(dll.to_list())  # [5, 4, 3, 2, 1]
```

## Requirements

- Python 3.6 or higher
- No external dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Created as a demonstration of doubly linked list implementation in Python.
