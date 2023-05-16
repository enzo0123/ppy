class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.nextE
        return " -> ".join(elements)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current.data
            current = current.nextE
        return None

    def delete(self, e):
        if not self.head:
            return

        if self.head.data == e:
            self.head = self.head.nextE
            self.size -= 1
            if not self.head:
                self.tail = None
            return

        current = self.head
        while current.nextE:
            if current.nextE.data == e:
                current.nextE = current.nextE.nextE
                self.size -= 1
                if not current.nextE:
                    self.tail = current
                return
            current = current.nextE

    def append(self, e, func=None):
        if not type(e) == Element:
            new_element = Element(e)
        else:
            new_element = e

        if not self.head:
            self.head = new_element
            self.tail = new_element
        elif not func:
            if new_element.data >= self.tail.data:
                self.tail.nextE = new_element
                self.tail = new_element
            elif new_element.data < self.head.data:
                new_element.nextE = self.head
                self.head = new_element
            else:
                current = self.head
                while current.nextE and current.nextE.data <= new_element.data:
                    current = current.nextE
                new_element.nextE = current.nextE
                current.nextE = new_element
        else:
            if func(new_element.data, self.tail.data):
                self.tail.nextE = new_element
                self.tail = new_element
            elif func(self.head.data, new_element.data):
                new_element.nextE = self.head
                self.head = new_element
            else:
                current = self.head
                while current.nextE and not func(current.nextE.data, new_element.data):
                    current = current.nextE
                new_element.nextE = current.nextE
                current.nextE = new_element

        self.size += 1
