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
        n = self.head

        while (n is not None):

            if (n.element == element):

                if (n == self.head):
                    self.remove_first()

                elif (n == self.tail):
                    self.remove_last()

                else:
                    m = n.previous
                    o = n.next
    
                    if (m is not None):
                        m.next = o
                    if (o is not None):
                        o.previous = m

                    self.length -= 1
    
                return

            n = n.next

        raise ValueError('Element is not in the list.')

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

    def __eq__(self, obj):
        return self.equals(obj)

    def equals(self, obj):
        if (type(obj) is DoublyLinkedList):
            if (len(self) == len(obj)):

                if (self.is_empty() and obj.is_empty()):
                    return True

                m = obj.head

                for i in self:
                    if (m.element != i):
                        return False
                    m = m.next

                return True

        return False

    def __len__(self):
        return self.length

    def size(self):
        return self.length

    def add_last(self, element):
        self.add(element)

    def add_first(self, element):
        
        node = self.Node(element)

        if (self.head is None):
            self.head = self.tail = node

        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

        self.length += 1

    def remove_last(self):
        if (self.tail is None):
            raise IndexError('List is empty')

        m = self.tail.previous

        if (m is not None):
            m.next = None
            self.tail = m
        else:
            self.head = self.tail = None   

        self.length -= 1

    def remove_first(self):
        if (self.head is None):
            raise IndexError('List is empty')

        m = self.head.next

        if (m is not None):
            m.previous = None
            self.head = m

        else:
            self.head = self.tail = None

        self.length -= 1

    def get_last(self):
        if (self.tail is None):
            raise IndexError('List is empty')

        return self.tail.element

    def get_first(self):
        if (self.head is None):
            raise IndexError('List is empty')

        return self.head.element

    def get_element(self, index):
        counter = 0

        if (self.length < index or index < 0):
            raise IndexError('Given index surpaces or is below list\'s length')

        for i in self:
            if (counter == index):
                return i

            counter += 1

    def clone(self):
        copy = DoublyLinkedList()

        for i in self:
        	copy.add(i)

        return copy

    def reverse(self):
        reverse = DoublyLinkedList()

        for i in self:
            reverse.add_first(i)

        return reverse

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

    def mergesort(self):
        pass

    def mergesort_list(list):
        pass