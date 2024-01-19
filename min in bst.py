 temp = root
    if root==None:
        return -1
    while temp:
        if temp.left:
            temp=temp.left
        else:
            return temp.data

