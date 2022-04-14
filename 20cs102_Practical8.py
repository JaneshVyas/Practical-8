class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def push(self, value):
        if self.head is None:
            self.head=Node(value)
        else:
            new=Node(value)
            new.next=self.head
            self.head=new

    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.value
            self.head=self.head.next
            return popped

    def isempty(self):
        if self.head==None:
            return True
        else:
            return False

    def traverse(self):
        iter=self.head
        if self.isempty():
            print("Empty Stack")
        else:
            while(iter!=None):
                print(iter.value,"->",end=" ")
                iter=iter.next
            return 

stack=Stack()
for i in range(1,11):
    stack.push(i)

stack.traverse()

for i in range(1,6):
    remove=stack.pop()
    print(" ")
    print(f"Popped-->{remove}")

stack.traverse()

