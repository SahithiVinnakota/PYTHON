stack=list()
def push():
    n=int(input("enter the number to be inserted: "))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
        print(n," is inserted ")
def pop():
    if len(stack)==0:
        print("List is empty")
    else:
        print(stack[0], "has been deleted")
        del stack[0]
def display():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("the elements in stack are")
        for ele in stack:
            print(ele)
        print("top of the stack",stack[0])
while(1):
    print("Choose any operation from below\n1-Push Operation\n2-Pop Operation\n3-Display")
    str=input()
    if str=='1':
        print("Push operation")
        push()
    elif str=='2':
        print("Pop operation")
        pop()
    elif str=='3':
        print("display elements")
    else:
        print("wrong input check your number")
        break