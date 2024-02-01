ele = None
    while stack1:
        stack2.append(stack1.pop())
    
    if stack2:
        ele = stack2.pop()
    
    while stack2:
        stack1.append(stack2.pop())
    
    return ele if ele else -
