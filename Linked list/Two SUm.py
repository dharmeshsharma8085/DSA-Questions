result = []
left = head
right = head
while right.next is not None:
    right = right.next
while left is not None and right is not None and left.data < right.data:
    total = left.data+right.data
    if total == target:
        reault.append((left.data,right.data))
        left = left.next
        right = right.prev
    elif total > target:
        right = right.prev
    else:
        left=left.next
return result