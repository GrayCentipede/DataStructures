import unittest
import random

from src.Queue import Queue

class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        q = Queue()

        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())

        self.assertEqual(q.peek(), 1)

        q.enqueue(2)
        self.assertNotEqual(q.peek(), 2)

    def test_dequeue(self):
        q = Queue()

        self.assertRaises(IndexError, q.dequeue)

        for i in range(10):
            q.enqueue(i)

        for i in range(9):
            self.assertEqual(q.peek(), i)
            q.dequeue()
            self.assertNotEqual(q.peek(), i)

        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_peek(self):
        q = Queue()

        self.assertRaises(IndexError, q.peek)

        q.enqueue(0)
        self.assertEqual(q.peek(), 0)

        q.enqueue(1)
        self.assertNotEqual(q.peek(), 1)
        self.assertEqual(q.peek(), 0)

        q.dequeue()
        self.assertEqual(q.peek(), 1)        

    def test_is_empty(self):
        q = Queue()

        self.assertTrue(q.is_empty())

        for i in range(1000):
            n = random.randint(0, 1000)
            q.enqueue(n)

        counter = 0
        while (not q.is_empty()):
            q.dequeue()
            counter += 1

        self.assertEqual(counter, 1000)

    def test_equals(self):
        qa = Queue()
        qb = Queue()

        self.assertEqual(qa, qb)

        for i in range(50):
            r = random.randint(1, 200)

            qa.enqueue(r)
            self.assertNotEqual(qa, qb)
            qb.enqueue(r)
            self.assertEqual(qa, qb)

        for i in range(50):
            qa.dequeue()
            self.assertNotEqual(qa, qb)
            qb.dequeue()
            self.assertEqual(qa, qb)

    def test_str(self):
        q = Queue()

        self.assertEqual(str(q), '')

        s = ''

        for i in range(50):
            r = random.randint(1, 200)

            q.enqueue(r)
            if (s == ''):
                s = str(r)
            else:
                s = str(r) + ' ' + s
                

        q.enqueue(929)
        s = '929 ' + s

        self.assertEqual(str(q), s)

        s = s[:-4]
        q.dequeue()

        self.assertEqual(str(q), s)

if __name__ == '__main__':
    unittest.main(verbosity = 2)