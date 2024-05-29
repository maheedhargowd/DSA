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
    
    def remove_last (self):
        if self.head is None :
            print('--NOTHING TO REMOVE-- ')
        else :
            current = self.head
            while current.next :
                current=current.next
            current.value = None
    
    

l=LinkedList()
a=Node(7)
b=Node(9)
c=Node(10)
d=Node(9)
l.add_node(a)
l.add_node(b)
l.add_node(c)
l.add_node(d)
l.remove_last()
current=l.head
while current :
    print(current.value)
    current=current.next