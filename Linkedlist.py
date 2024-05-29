class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

class LinkedList : 
    def __init__(self,head=None):
        self.head=head
        
    def add_node (self,node):
        if self.head is None : 
            self.head = node
        else : 
            counter = self.head 
            while counter.next:
                counter =counter.next
            counter.next=node

l=LinkedList()
a=Node(1)
b=Node(5)
l.add_node(a)
l.add_node(b)

print(l)
current =l.head
while current :
    print(current.value)
    current=current.next