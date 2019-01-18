class DoublyLinkedList(object):

    class Node(object):

        element  = None
        next     = None
        previous = None

        def __init__(self, element):
            self.element = element

    head   = None
    tail   = None
    length = 0

    def add(self, element):

        node = self.Node(element)

        if (self.head is None):
            self.head = self.tail = node

        else:
        	node.previous = self.tail
        	self.tail.next = node
        	self.tail = node

        self.length += 1

    def delete(self, element):
        pass

    def is_empty(self):
        return (self.length == 0)

    def get_elements(self):
        return self.length

    def clear(self):
        self.length = 0
        self.head = self.tail = None

    def __iter__(self):
        self.iter_node = self.head
        return self

    def __next__(self):
        if self.iter_node is not None:
            element = self.iter_node.element
            self.iter_node = self.iter_node.next
            return element

        else:
            raise StopIteration

    def __str__(self):
        if (self.length == 0):
            return '[]'

        s = '['
        counter = 0

        for i in self:
            counter += 1

            if (counter < self.length):
                s += str(i) + ', '
            else:
                s += str(i) + ']'    

        return s

    def __repr__(self):
        return str(self)

    def __eq__(self, object):
        pass

    def equals(self, object):
        pass

    def __len__(self):
        return self.length

    def size(self):
        return self.length

    def add_last(self, element):
        self.add(element)

    def add_first(self, element):
        pass

    def remove_last(self):
        pass

    def remove_first(self):
        pass

    def get_last(self):
        return self.tail.element

    def get_first(self):
        return self.head.element

    def get_element(self, index):
        counter = 0

        for i in self:
            if (counter == index):
                return i

            counter += 1


    def clone(self):
        pass

    def reverse(self):
        pass

    def index_of(self, element):
        counter = 0

        for i in self:
            if (i == element):
                return counter

            counter += 1

        raise ValueError(str(element) + 'is not in list')

    def contains(self, element):
        counter = 0

        for i in self:
            if (i == element):
                return True

            counter += 1

        return False