
def enqueue():
    n=int(input("Enter the element to be inserted"))
    queue.append(n)
    print()
def dequeue():
    if len(queue)==0:
        print("queue is empty")
        print()
    else:
        print(queue [0],"is deleted")
        del queue[0]
        print()
def display():
    if len(queue)==0:
        print("queue is empty")
    else:
        print("the elements in the queue are: ")
        for ele in queue:
            print(ele,end=" ")
            print()
        print("front of the queue is",queue[0])
        print("rear of the queue is",queue[-1])
        print()
queue=list()
while(1):
    option=input("Choose the operation\n1.Enqueue operation\n2.Dequeue Operation\n3.Display Operation\n4.Exit\n")
    if option=='1':
        print("Enqueue opertaion")
        enqueue()
    elif option=='2':
        print("Dequeue operation")
        dequeue()
    elif option=='3':
        print("Display Operation")
        display()
    else:
        break
