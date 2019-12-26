import random, math

class ArraySorter(object):

    def swap(self, i, j, array):
        temp     = array[i]
        array[i] = array[j]
        array[j] = temp

    def bubble_sort(self, array):
        n      = len(array)

        if (n <= 1):
            return array

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

        if (n <= 1):
            return array

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
        n = len(array)

        if (n <= 1):
            return array

        half = int(n/2)

        a = array[:half]
        b = array[half:]

        return self.merge(self.merge_sort(a), self.merge_sort(b))

    def merge(self, a, b):
        if not a:
            return b
        elif not b:
            return a

        n = len(a)
        m = len(b)

        new_array = []

        while a and b:
            max_a = a[-1]
            max_b = b[-1]

            if (max_a > max_b):
                new_array.append(max_a)
                a.pop()
            elif (max_b > max_a):
                new_array.append(max_b)
                b.pop()
            else:
                new_array.append(max_a)
                new_array.append(max_b)
                a.pop()
                b.pop()

        if not a and not b:
            return new_array.reverse()
        elif not a:
            while b:
                new_array.append(b.pop())
        else:
            while a:
                new_array.append(a.pop())

        return new_array.reverse()


    def insertion_sort(self, array):
        n = len(array)

        if (n <= 1):
            return array

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
        n = len(array)

        if (n <= 1):
            return array

        num_buckets = math.ceil(math.sqrt(n))

        max_array = max(array)

        divider = math.ceil((max_array + 1) / num_buckets)

        buckets = [ [] for i in range(num_buckets) ]

        for i in range(n):
            j = math.floor(array[i] / divider)
            buckets[j].append(array[i])

        new_array = []

        for bucket in buckets:
            if bucket:
                sorted_bucket = self.insertion_sort(bucket)
                new_array.extend(sorted_bucket)

        return new_array
