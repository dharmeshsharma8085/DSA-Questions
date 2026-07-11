class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
class SLL:
    def __init__(self):
        self.head=None

#Append  --: Added to the last og SLL

    def Append(self,val):
        new_node=Node(val)
        #SLL can be empt
        if self.head==None:
            self.head=new_node
        # SLL i not empty
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
            
        #T.C O(n) S.C =O(1)
        
#TRAVERSAL
    def Traverse(self):
        if self.head is None:
            print("SLL is empty")
        else:
            current=self.head
            while current is not None:
                print(current.val,end=" ")
                current=current.next
            print()
        # T.C =O(n) , S.C = O(1)
        
    #Insertion at specfic postion
    def insert_at( self , val , position):
        new_node = Node(val)
        if position ==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count <position:
                prev_node = current
                current= current.next
                count +=1
            prev_node.next=new_node
            new_node.next= current
            
    # deltetion 
    def delelte(self ,val):
        temp = self.head 
        if temp.next is not None:
            self.head = temp.next
            del temp
            return 
        else:
            found = False 
            prev = None
            while temp is not None:
                if temp.val == val:
                    found = True
                prev = temp
                temp = temp.next
            if found :
                prev.next == temp.next
                del temp
                return
            else:
                print("Node Not Found !!!!!!!!!!!!!!!!!")
                
        
    
    
    
s11=SLL()
s11.Append(10)
s11.Append(20)
s11.Append(30)
s11.Append(40)
s11.Append(1)
s11.Traverse()
s11.insert_at(5,2)
s11.Traverse()


