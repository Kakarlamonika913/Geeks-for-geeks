 queue = deque([root])
    stack = deque([])
    while queue:
        temp = queue.popleft()
        stack.appendleft(temp.data)
        if temp.right:
            queue.append(temp.right)
        if temp.left:
            queue.append(temp.left)
    return stack

