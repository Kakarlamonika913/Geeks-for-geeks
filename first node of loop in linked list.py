 slow = head
        fast = head
        temp = head
        while fast:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                return -1
            if fast == slow:
                while slow:
                    if slow == temp:
                        return temp.data

                    temp = temp.next
                    slow = slow.next
