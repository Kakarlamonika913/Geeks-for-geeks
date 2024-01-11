 curr = head
        prev_node = None
        while curr!=None:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
            
        curr = prev_node
        return curr
