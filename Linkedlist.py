
class Node :
    def __init__(self,value,next = None) :
        self.value=value
        self.next=next
a=Node(10)

class LinkedList :
    def __init__(self,head=None):
        self.head=head
        
    def add_node(self,node):
        if self.head is None :
            self.head = node 
        else :
            current =self.head
            while current.next : 
                current = current.next
            
            current.next = node 
    
    def remove_node (self,node):
        if self.head is None :
            print('-- Given node is not avialable --')
        elif self.head == node :
            self.head = self.head.next
        else :
            current = self.head
            while current.next and current.next != node :
                current =current.next 
            current.next = node.next

    def remove_last(self):
        if self.head is None :
            print('-- Given node is not available')
        else : 
            current = self.head
            while current.next.next :
                current = current.next 
            current.next = None
            
        
l=LinkedList()
a=Node(1)
l.add_node(a)
b=Node(2)
l.add_node(b)
c=Node(3)
l.add_node(c)
d=Node(3)
l.add_node(d)


l.remove_last()
current = l.head
while current :
    print(current.value)
    current = current.next        