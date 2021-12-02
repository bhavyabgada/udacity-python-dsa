#Single Unit Linked List

class Element(object):
    def __init__(self, value):
        self.value = 'value'
        self.next = None

#Linked List Class

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    #Adding Element at the end of the Linked List

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    

