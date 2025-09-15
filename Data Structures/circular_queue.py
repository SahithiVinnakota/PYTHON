class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=self.rear=-1
    def enqueue(self,data):
        if((self.rear+1)%self.size==self.front):
            print("Queue is empty")
        elif(self.front==-1):
            self.rear=self.front=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if (self.front==-1):
            print("Queue is Empty")
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=self.rear==-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            print("Queue Elements")
            
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                icq.enqueue(50)  # Queue is full here
cq.display()
print("Dequeued:", cq.dequeue())
cq.enqueue(60)
cq.display()


