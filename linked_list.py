class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single_Linked_list:
    def __init__(self):
        self.head=None
#insert at beginning
    def insert_at_beginning(self,data): 
        nb= Node(data)
        nb.next = self.head
        self.head=nb
#insert at end
    def insert_at_end(self,data):
        ne= Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next = ne
#insert at specific location
    def insert_at_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np
#deletion at beginning
    def del_at_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
#deletion at end
    def del_at_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None   
#deletion at specific location
    def del_at_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None        

    def display(self):
        if self.head is None:
            print("Empty linked list")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
L = Single_Linked_list()
n=Node(10)
L.head=n
n1= Node(20)
n.next=n1
n2 = Node(30)
n1.next=n2
L.insert_at_beginning(5)
L.insert_at_end(60)
L.insert_at_pos(2,15)
L.insert_at_pos(3,40)
L.insert_at_pos(4,50)
L.del_at_beginning()
L.del_at_end
L.del_at_pos(2)
L.display()