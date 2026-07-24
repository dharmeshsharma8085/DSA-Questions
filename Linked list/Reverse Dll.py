if head.next is None:
    return head
current = head
prev = None
while current is not None:
    front = current.next
    current.prev = front
    prev = current
    current = front
return prev