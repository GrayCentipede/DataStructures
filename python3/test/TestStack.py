import unittest
import random

from src.Stack import Stack

class TestStack(unittest.TestCase):

    def test_push(self):
        s = Stack()

        self.assertTrue(s.is_empty())
        s.push('a')
        self.assertFalse(s.is_empty())

        for i in range(50):
            n = random.randint(0, 1000)

            s.push(n)
            self.assertEqual(s.peek(), n)

    def test_pop(self):
        s = Stack()

        self.assertRaises(IndexError, s.pop)

        for i in range(50):
            s.push(i)

        for i in range(50):
            k = s.pop()

            self.assertEqual(k, (49 - i))

        self.assertRaises(IndexError, s.pop)

    def test_peek(self):
        s = Stack()

        self.assertRaises(IndexError, s.peek)

        s.push(0)
        self.assertEqual(s.peek(), 0)

        s.push(1)
        self.assertEqual(s.peek(), 1)
        s.pop()
        self.assertNotEquals(s.peek(), 1)

    def test_is_empty(self):
        s = Stack()

        self.assertTrue(s.is_empty())

        for i in range(10):
            s.push(i)

        self.assertFalse(s.is_empty())

        for i in range(10):
            s.pop()

        self.assertTrue(s.is_empty())

    def test_equals(self):
        sa = Stack()
        sb = Stack()
        sc = Stack()

        self.assertEqual(sa, sb)

        for i in range(50):
            n = random.randint(1, 1000)

            sa.push(n)

        self.assertNotEquals(sa, sb)

        while (not sa.is_empty()):
            k = sa.pop()
            sb.push(k)
            sc.push(k)

        self.assertEqual(sb, sc)

        while (not sb.is_empty()):
            k = sb.pop()
            sa.push(k)

        while (not sc.is_empty()):
            k = sc.pop()
            sb.push(k)

        self.assertEqual(sa, sb)


    def test_str(self):
        s = Stack()

        self.assertEqual(str(s), '')

        for i in range(5):
            s.push(i)

        self.assertEqual(str(s), '4\n3\n2\n1\n0')

        s.pop()
        s.pop()

        self.assertEqual(str(s), '2\n1\n0')

        s.pop()
        s.push(300)
        s.push(10)

        self.assertEqual(str(s), '10\n300\n1\n0')

        while (not s.is_empty()):
            s.pop()

        n = random.randint(1, 365)

        s.push(n)

        self.assertEqual(str(s), str(n))

if __name__ == '__main__':
    unittest.main(verbosity = 2)