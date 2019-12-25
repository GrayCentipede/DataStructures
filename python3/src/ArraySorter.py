import random

class ArraySorter(object):

    def swap(self, i, j, array):
        temp     = array[i]
        array[i] = array[j]
        array[j] = temp

    def bubble_sort(self, array):
        n      = len(array)
        swaped = True

        while swaped:
            swaped = False

            for j in range(n - 1):
                if (array[j] > array[j + 1]):
                    self.swap(j, j + 1, array)
                    swaped = True

            if not swaped:
                break

        return array


    def selection_sort(self, array):
        n = len(array)

        for i in range(n - 1):
            min_index = i
            for j in range(i, n):
                if (array[j] < array[min_index]):
                    min_index = j
            self.swap(i, min_index, array)

        return array

    def quick_sort(self, array):
        n = len(array)

        if (n <= 1):
            return array

        pivot  = random.randint(0, n - 1)

        lesser  = []
        greater = []

        for k in range(n - 1):
            if (k != pivot):
                if (array[k] <= array[pivot]):
                    lesser.append(array[k])
                else:
                    greater.append(array[k])

        lesser  = self.quick_sort(lesser)
        greater = self.quick_sort(greater)

        return lesser + [array[pivot]] + greater

    def merge_sort(self, array):
        pass

    def insertion_sort(self, array):
        n = len(array)

        for i in range(1, n):
            if (array[i-1] > array[i]):
                self.swap(i-1, i, array)
                for j in range(i-1):
                    k = (i - 1) - j
                    if (array[k - 1] > array[k]):
                        self.swap(k-1, k, array)
                    else:
                        break

        return array

    def bucket_sort(self, array):
        pass
