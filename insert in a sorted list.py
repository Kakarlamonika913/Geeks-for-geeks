new_node=Node(key)
    curr=head1
    if key<curr.data:
        new_node.next=curr
        return new_node
    while curr.next and key>curr.next.data:
        curr=curr.next
    temp=curr.next
    curr.next=new_node
    new_node.next=temp
    return head1
