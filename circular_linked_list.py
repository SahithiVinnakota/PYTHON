class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid position!")
            return
        new_node = Node(data)
        if position == 1:
            self.insert_at_beginning(data)
            return
        temp = self.head
        count = 1
        while count < position - 1 and temp.next != self.head:
            temp = temp.next
            count += 1
        if count == position - 1:
            new_node.next = temp.next
            temp.next = new_node
        else:
            print("Position out of bounds")

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            prev = None
            temp = self.head
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            prev.next = self.head

    def delete_at_position(self, position):
        if not self.head or position <= 0:
            print("Invalid position or empty list")
            return
        if position == 1:
            self.delete_at_beginning()
            return
        temp = self.head
        count = 1
        prev = None
        while count < position and temp.next != self.head:
            prev = temp
            temp = temp.next
            count += 1
        if count == position:
            prev.next = temp.next
        else:
            print("Position out of bounds")

    def display(self):
        if not self.head:
            print("List is empty!")
            return
        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_beginning(5)
cll.insert_at_position(15, 3)
cll.display()

cll.delete_at_beginning()
cll.display()

cll.delete_at_end()
cll.display()

cll.delete_at_position(2)
cll.display()
