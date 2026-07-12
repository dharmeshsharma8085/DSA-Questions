# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = self.head
        while temp is not None:
            temp=temp.next
            n+=1
        temp=self.head
        if count%2==0:
            for i in range(0,(count+2)//2):
                temp=temp.next
        else:
            for i in range(0,n//2):
                temp=temp.next
        return temp
    
# optimal

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while ( fast is not None) and (fast.next is not None):
            slow=slow.next
            fast=fast.next.next
        return slow

