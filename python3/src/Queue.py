class Queue(object):
    
    class Node(object):
        element = None
        next    = None

        def __init__(self, element):
            self.element = element

    head = None
    tail = None

    def enqueue(self, element):
        node = self.Node(element)

        if (self.head is None):
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if (self.head is None):
            raise IndexError('Queue is empty')

        e = self.head.element

        if (self.head.next is None):
            self.head = self.tail = None

        else:
            self.head = self.head.next

        return e


    def peek(self):
        if (self.head is None):
            raise IndexError('Queue is empty')

        return self.head.element

    def is_empty(self):
        return (self.head is None)

    def equals(self, obj):
        if (type(obj) is Queue):

            if (obj.is_empty() and self.is_empty()):
                return True

            n = self.head
            m = obj.head

            while ((m is not None) or (n is not None)):

                a = (n is None and m is not None)
                b = (n is not None and m is None) 

                if (a or b or (n.element != m.element)):
                    return False

                n = n.next
                m = m.next

            return True

        return False

    def __eq__(self, obj):
        return self.equals(obj)

    def __str__(self):
        if (self.head is None):
            return ''

        n = self.head
        s = str(n.element)

        while (n.next is not None):
            m = n.next
            s = str(m.element) + ' ' + s

            n = n.next

        return s

    def __repr__(self):
        if (self.head is None):
            return '[]'

        n = self.head
        s = str(n.element) + ']'

        while (n.next is not None):
            m = n.next
            s = str(m.element) + ', ' + s

            n = n.next

        return '[' + s