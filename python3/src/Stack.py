class Stack(object):

    class Node(object):
        element = None
        next    = None

        def __init__(self, element):
            self.element = element

    head = None

    def push(self, element):
        node = self.Node(element)

        if (self.head is None):
            self.head = node

        else:
            temp = self.head
            self.head = node
            node.next = temp

    def pop(self):
        if (self.head is None):
            raise IndexError('Empty stack')

        e = self.head.element

        if (self.head.next is None):
            self.head = None
        else:
            self.head = self.head.next

        return e

    def peek(self):
        if (self.head is None):
            raise IndexError('Empty stack')

        return self.head.element

    def is_empty(self):
        return (self.head is None)

    def equals(self, obj):
        if (type(obj) is Stack):

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


    def __eq__(self, obj):
        return self.equals(obj)

    def __str__(self):
        s = ""

        n = self.head

        if (n is None):
            return s

        while (n is not None):
            if (n.next is None):
                s += str(n.element)
            else:
                s += str(n.element) + '\n'

            n = n.next

        return s

    def __repr__(self):
        n = self.head

        if (n is None):
            return '[]'

        r = "["

        while (n is not None):
            if (n.next is None):
                r += str(n.element)
            else:
                r += str(n.element) + ', '

            n = n.next

        return r + ']'