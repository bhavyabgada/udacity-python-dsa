#Single Unit Linked List
class Element(object):
    def __init__(self, value):
        self.value = value
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
    
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

#Test Cases
#Setting up some elements
e0 = Element(0)
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

#Setting up the linked list
ll = LinkedList(e0)
ll.append(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

#function to print the linked list {expectedOutput : 0 ==> 1 ==> 2 ==> 3 ==> 4}
def printing(ll):
    if ll.head == None:
        return 'Linked List is Empty.'
    else:
        current = ll.head
        while current.next:
            print(current.value, end=' ==> ')
            current = current.next
        print(current.value)

#testing the printing function.
printing(ll)

#testing getposition
print(ll.get_position(3).value)