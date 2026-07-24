class Node:
    def __init__(self,val):
        self.val =val
        self.next = None
        self.prev = None
        
n1 = Node(10)
n2 = Node(15)
n3=Node(8)

n1.next=n2 
n1.prev=None
n2.next=n3 
n2.prev=n1
n3.next= None 
n3.prev=n2



print(n1.next.next)
        
        