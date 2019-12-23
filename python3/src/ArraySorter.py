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
        pass

    def merge_sort(self, array):
        pass

    def insertion_sort(self, array):
        pass

    def bucket_sort(self, array):
        pass
