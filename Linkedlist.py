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
    
    def remove_last(self):
        if self.head is None :
            print('--NOTHING TO REMOVE-- ')
        elif self.head.next is None :
            self.head = None
        else : 
            current = self.head
            while current.next.next :
                current=current.next
            current.next = None


l=LinkedList()
a=Node(10)
l.add_node(a)
b=Node(2)
l.add_node(b)
c=Node(9)
l.add_node(c)

l.remove_last()
current=l.head
while current :
    print(current.value)
    current=current.next 