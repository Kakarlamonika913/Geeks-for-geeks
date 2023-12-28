new_stack = []
        count = sizeOfStack - 1
        middle = count//2
        while count != middle:
            new_stack.append(s.pop())
            count -= 1
        s.pop()
        while new_stack:
            s.append(new_stack.pop())
        return s
