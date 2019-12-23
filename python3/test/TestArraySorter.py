import unittest
import random

from src.ArraySorter import ArraySorter

class TestArraySorter(unittest.TestCase):

    def is_sorted(self, array):
        n = len(array)

        for i in range(n - 1):
            if (array[i] > array[i + 1]):
                return False

        return True

    def generate_random_array(self, n):
        x = []

        for i in range(n):
            m = random.randint(0, 360)
            x.append(m)

        return x

    def test_bubble_sort(self):
        a = self.generate_random_array(10)
        a.append(a[-1] - 1)

        self.assertFalse(self.is_sorted(a))

        sorter = ArraySorter()
        a = sorter.bubble_sort(a)
        self.assertTrue(self.is_sorted(a))

        a.append(a[-1] - 1)
        self.assertFalse(self.is_sorted(a))

    def test_selection_sort(self):
        a = self.generate_random_array(10)
        a.append(a[-1] - 1)

        self.assertFalse(self.is_sorted(a))

        sorter = ArraySorter()
        a = sorter.selection_sort(a)
        self.assertTrue(self.is_sorted(a))

        a.append(a[-1] - 1)
        self.assertFalse(self.is_sorted(a))

    def test_quick_sort(self):
        a = self.generate_random_array(10)
        a.append(a[-1] - 1)

        self.assertFalse(self.is_sorted(a))

        sorter = ArraySorter()
        a = sorter.test_quick_sort(a)
        self.assertTrue(self.is_sorted(a))

        a.append(a[-1] - 1)
        self.assertFalse(self.is_sorted(a))

    def test_merge_sort(self):
        a = self.generate_random_array(10)
        a.append(a[-1] - 1)

        self.assertFalse(self.is_sorted(a))

        sorter = ArraySorter()
        a = sorter.merge_sort(a)
        self.assertTrue(self.is_sorted(a))

        a.append(a[-1] - 1)
        self.assertFalse(self.is_sorted(a))

    def test_insertion_sort(self):
        a = self.generate_random_array(10)
        a.append(a[-1] - 1)

        self.assertFalse(self.is_sorted(a))

        sorter = ArraySorter()
        a = sorter.insertion_sort(a)
        self.assertTrue(self.is_sorted(a))

        a.append(a[-1] - 1)
        self.assertFalse(self.is_sorted(a))

    def test_bucket_sort(self):
        a = self.generate_random_array(10)
        a.append(a[-1] - 1)

        self.assertFalse(self.is_sorted(a))

        sorter = ArraySorter()
        a = sorter.bucket_sort(a)
        self.assertTrue(self.is_sorted(a))

        a.append(a[-1] - 1)
        self.assertFalse(self.is_sorted(a))

if __name__ == '__main__':
    unittest.main(verbosity = 2)
