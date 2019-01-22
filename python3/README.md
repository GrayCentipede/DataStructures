# Python 3.7.1
## Data structures:
* Doubly Linked List. [Definition](https://en.wikipedia.org/wiki/Doubly_linked_list)
* Stack. [Definition](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
* Queue. [Definition](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))

## Unit Testing & Importing Modules
To do the following you must be in the ```python3``` directory.

### Unit Testing
To execute any unit test you must enter the following command:
```
python3 -m test.Test[Data Structure]
```

Example given:
```
python3 -m test.TestDoublyLinkedList
```
Introducing the previous command will show the following on the terminal:
```
test_add (__main__.TestDoublyLinkedList) ... ok
test_add_first (__main__.TestDoublyLinkedList) ... ok
test_add_last (__main__.TestDoublyLinkedList) ... ok
test_clear (__main__.TestDoublyLinkedList) ... ok
test_clone (__main__.TestDoublyLinkedList) ... ok
test_contains (__main__.TestDoublyLinkedList) ... ok
test_delete (__main__.TestDoublyLinkedList) ... ok
test_equals (__main__.TestDoublyLinkedList) ... ok
test_get_element (__main__.TestDoublyLinkedList) ... ok
test_get_elements (__main__.TestDoublyLinkedList) ... ok
test_get_first (__main__.TestDoublyLinkedList) ... ok
test_get_last (__main__.TestDoublyLinkedList) ... ok
test_index_of (__main__.TestDoublyLinkedList) ... ok
test_is_empty (__main__.TestDoublyLinkedList) ... ok
test_iterator (__main__.TestDoublyLinkedList) ... ok
test_len (__main__.TestDoublyLinkedList) ... ok
test_remove_first (__main__.TestDoublyLinkedList) ... ok
test_remove_last (__main__.TestDoublyLinkedList) ... ok
test_reverse (__main__.TestDoublyLinkedList) ... ok
test_str (__main__.TestDoublyLinkedList) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.043s

OK
```

### Importing Modules
If for some reason you want to use a data structure then you only have to write the following in your script:
```
from scr.[Data Structure] import [Data Structure]
```

Example given:
```
from scr.DoublyLinkedList import DoublyLinkedList
```