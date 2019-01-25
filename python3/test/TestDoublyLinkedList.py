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

        self.assertRaises(ValueError, l.delete, 0)

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
        self.assertRaises(ValueError, l.index_of, 4)
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

    def test_equals(self):
        la = DoublyLinkedList()
        lb = DoublyLinkedList()

        self.assertEqual(la, lb)

        for i in range(10):
        	n = random.randrange(1, 360)
        	la.add(n)

        self.assertNotEqual(la, lb)

        for i in la:
        	lb.add(i)

        self.assertEqual(la, lb)

        lb.remove_last()
        self.assertNotEqual(la, lb)

        la.remove_last()
        self.assertEqual(la, lb)

        self.assertNotEqual(la, None)

    def test_len(self):
        l = DoublyLinkedList()

        self.assertEqual(len(l), 0)

        for i in range(100):
        	l.add(i)

        self.assertEqual(len(l), 100)

        for i in range(50):
        	l.remove_first()

        self.assertEqual(len(l), 50)

    def test_add_last(self):
        la = DoublyLinkedList()
        lb = DoublyLinkedList()

        for i in range(1000):
        	n = random.randint(1, 360)
        	la.add(n)
        	lb.add_last(n)

        self.assertEqual(la, lb)

    def test_add_first(self):
        la = DoublyLinkedList()
        lb = DoublyLinkedList()

        for i in range(1000):
        	n = random.randint(1, 360)
        	la.add(n)
        	lb.add_first(n)

        self.assertEqual(la, lb.reverse())

    def test_remove_last(self):
        l = DoublyLinkedList()

        self.assertTrue(l.is_empty())

        l.add('a')
        l.add('b')
        l.add('c')

        self.assertEqual(len(l), 3)

        l.remove_last()
        self.assertEqual(len(l), 2)
        self.assertEqual(l.get_last(), 'b')

        l.remove_last()
        self.assertEqual(len(l), 1)
        self.assertEqual(l.get_last(), 'a')

        l.remove_last()
        self.assertRaises(IndexError, l.remove_last)
        self.assertEqual(len(l), 0)
        self.assertTrue(l.is_empty())


    def test_remove_first(self):
        l = DoublyLinkedList()

        self.assertTrue(l.is_empty())

        l.add('a')
        l.add('b')
        l.add('c')

        self.assertEqual(len(l), 3)

        l.remove_first()
        self.assertEqual(len(l), 2)
        self.assertEqual(l.get_first(), 'b')

        l.remove_first()
        self.assertEqual(len(l), 1)
        self.assertEqual(l.get_first(), 'c')

        l.remove_first()
        self.assertRaises(IndexError, l.remove_first)
        self.assertEqual(len(l), 0)
        self.assertTrue(l.is_empty())

    def test_get_last(self):
        l = DoublyLinkedList()

        self.assertRaises(IndexError, l.get_last)

        for i in range(50):
            l.add(i)
            self.assertEqual(l.get_last(), i)

    def test_get_first(self):
        l = DoublyLinkedList()

        self.assertRaises(IndexError, l.get_first)

        for i in range(50):
            l.add_first(i)
            self.assertEqual(l.get_first(), i)

    def test_get_element(self):
        l = DoublyLinkedList()

        self.assertRaises(IndexError, l.get_element, 10)

        for i in range(101):
        	l.add(i)

        for i in range(25):
        	n = random.randint(0, 100)
        	self.assertEqual(l.get_element(n), n)


    def test_clone(self):
        la = DoublyLinkedList()
        lb = la.clone()

        self.assertEqual(la, lb)

        for i in range(50):
        	lb.add(i)

        self.assertNotEqual(la, lb)

        la = lb.clone()

        self.assertEqual(la, lb)

    def test_reverse(self):
        la = DoublyLinkedList()
        lb = DoublyLinkedList()

        self.assertEqual(la, la.reverse())

        for i in range(101):
        	la.add(i)
        	lb.add((100 - i))

        self.assertNotEqual(la, lb)
        self.assertEqual(la, lb.reverse())
        self.assertEqual(la.reverse(), lb)
        self.assertNotEqual(la.reverse(), lb.reverse())

    def test_index_of(self):
        l = DoublyLinkedList()

        self.assertRaises(ValueError, l.index_of, 'a')

        for i in range(5):
        	l.add(1)

        self.assertEqual(l.index_of(1), 0)

        l.remove_last()
        l.add(2)

        self.assertEqual(l.index_of(2), 4)

        l.remove_first()
        l.add_first(2)

        self.assertEqual(l.index_of(1), 1)

    def test_contains(self):
        l = DoublyLinkedList()

        for i in range(5):
        	self.assertFalse(l.contains(i))
        	l.add(i)
        	self.assertTrue(l.contains(i))

    def test_mergesort(self):
        pass

    def test_mergesort_list(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity = 2)