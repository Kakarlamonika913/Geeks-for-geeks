#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    # Code here
    temp=head.next
    while(temp!=None and temp!=head):
        temp=temp.next
    return temp==head
    

