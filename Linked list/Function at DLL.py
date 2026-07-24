class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        
class DLL:
    def __init__(self):
        self.head =None
    
    # insert at head
    def insert_at_head(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next=self.head
            self.head.prev= new_node
            self.head= new_node
            
    # Append
    def append(self,val):
        new_node = Node(val)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
            new_node.next=None
            
    #Insert in between
    def insert_at(self , val ,postion):
        new_node=Node(val)
        if postion == 0:
            self.insert_at_head(val):
            return
        current = self.head
        count =0
        while current and count<postion -1:
            current is current.next
            count+=1
            
            if current is None :
                print("Postions out of bound")
                return
            
        new_node.next = current.next
        new_node.prev = current 
        if current.next:
            current.nect.prev = new_node
        current.next = new_node               
            
        
            
    
    
dll=DLL()
dll.insert_at_head(20) 
dll.append(12)

    
        
    
             
            