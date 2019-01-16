import unittest
import random

from src.DoublyLinkedList import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):

    def test_add(self):
        l = DoublyLinkedList()

        self.assertTrue(l.is_empty())

        l.add(0)
        self.assertEqual(l.get_first(), 0)
        self.assertEqual(l.get_last(), 0)
        self.assertEqual(l.get_elements(), 1)

        l.add(1)
        self.assertEqual(l.get_last(), 1)
        self.assertNotEqual(l.get_first(), 1)
        self.assertEqual(l.get_first(), 0)
        self.assertEqual(l.get_elements(), 2)

        l.add(2)
        self.assertEqual(l.get_last(), 2)
        self.assertEqual(l.get_first(), 0)
        self.assertEqual(l.index_of(1), 1)
        self.assertEqual(l.get_elements(), 3)

        self.assertFalse(l.is_empty())

    def test_delete(self):
        l = DoublyLinkedList()

        self.assertRaises(IndexError, l.delete, 0)

        for i in range(5):
            l.add(i)
            self.assertTrue(l.contains(i))

        l.delete(2)
        self.assertFalse(l.contains(2))
        self.assertEqual(l.index_of(1), 1)
        self.assertEqual(l.index_of(3), 2)
        self.assertEqual(l.get_elements(), 4)

        l.delete(0)
        self.assertFalse(l.contains(0))
        self.assertEqual(l.get_first(), 1)
        self.assertEqual(l.index_of(3), 1)
        self.assertEqual(l.get_elements(), 3)

        l.delete(4)
        self.assertFalse(l.contains(4))
        self.assertEqual(l.get_last(), 3)
        self.assertEqual(l.get_first(), 1)
        self.assertEqual(l.index_of(4), -1)
        self.assertEqual(l.get_elements(), 2)

        l.delete(1)
        self.assertFalse(l.contains(1))
        self.assertEqual(l.get_first(), 3)
        self.assertEqual(l.get_last(), 3)
        self.assertEqual(l.get_elements(), 1)

        l.delete(3)
        self.assertTrue(l.is_empty())
        self.assertEqual(l.get_elements(), 0)


    def test_is_empty(self):
        l = DoublyLinkedList()

        self.assertTrue(l.is_empty())

        for i in range(10):
            l.add(i)

        self.assertFalse(l.is_empty())

        for i in range(10):
            l.delete(i)

        self.assertTrue(l.is_empty())

    def test_get_elements(self):
        l = DoublyLinkedList()

        self.assertEqual(l.get_elements(), 0)

        for i in range(100):
            l.add(i)
            self.assertEqual(l.get_elements(), (i + 1))

        for i in range(100):
            l.delete(i)
            self.assertEqual(l.get_elements(), (99 - i))

    def test_clear(self):
        l = DoublyLinkedList()

        self.assertTrue(l.is_empty())

        for i in range(1000):
            l.add(i)

        self.assertFalse(l.is_empty())

        l.clear()

        self.assertTrue(l.is_empty())

    def test_iterator(self):
        l = DoublyLinkedList()

        for i in range(1000):
            l.add(i)

        k = 0
        for i in l:
            self.assertEqual(i, k)
            k += 1

        self.assertEqual(k, 1000) 


    def test_str(self):
        l = DoublyLinkedList()

        correct_str = "["
        
        for i in range(99):
        	n = random.randrange(1, 360)
        	l.add(n)
        	correct_str += str(n) + ", "

        n = random.randrange(1, 360)
        l.add(n)
        correct_str += str(n) + "]"

        self.assertEqual(str(l), correct_str)


    def test_repr(self):
        pass

    def test_eq(self):
        pass

    def test_equals(self):
        pass

    def test_len(self):
        pass

    def test_size(self):
        pass

    def test_add_last(self):
        pass

    def test_add_first(self):
        pass

    def test_remove_last(self):
        pass

    def test_remove_first(self):
        pass

    def test_get_last(self):
        pass

    def test_get_first(self):
        pass

    def test_get_element(self):
        pass

    def test_clone(self):
        pass

    def test_reverse(self):
        pass

    def test_index_of(self):
        pass

    def test_contains(self):
        pass

if __name__ == '__main__':
	unittest.main()