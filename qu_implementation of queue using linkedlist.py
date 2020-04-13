import gc
#class to create nodes 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#class to implement queue using linkedlist
class Queue_LinkedList:
    def __init__(self):
        #initially front and rear points to null
        self.front=None
        self.rear=None
    #function to check empty queue
    def isEmpty(self):
        if self.front==None:
            return True
        else:
            return False
    #function to insert an element into queue at rear end
    def Enqueue(self,data):
        newnode=Node(data)
        #if queue is empty make front and rear points to newnode
        if self.isEmpty():
            self.front=newnode
            self.rear=newnode
            return
        #else insert newnode at rear end
        self.rear.next=newnode
        self.rear=newnode
    #function to remove element from queue at front end
    def Dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        #if queue contains single element remove it and make front and rear point to null
        elif self.front==self.rear:
            temp=self.front
            self.front=None
            self.rear=None
            gc.collect()
            return temp.data
        temp=self.front
        self.front=self.front.next
        return temp.data
if __name__=="__main__":
    queue=Queue_LinkedList()
    queue.Enqueue(10)
    queue.Enqueue(20)
    queue.Enqueue(30)
    print("dequeued element is",queue.Dequeue())
    print("dequeued element is",queue.Dequeue())
    print("dequeued element is",queue.Dequeue())
    print("dequeued element is",queue.Dequeue())
    
    
