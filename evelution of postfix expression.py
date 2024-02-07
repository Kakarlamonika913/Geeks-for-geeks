 stack=[]
        for i in s:
            if i in ["+","*","/","-"]:
                y=stack.pop()
                x=stack.pop()
                if i=="+":
                    stack.append(x+y)
                elif i=="*":
                    stack.append(x*y)
                elif i=="-":
                    stack.append(x-y)
                else:
                    stack.append(x//y)
            else:
                stack.append(int(i))
        return stack[-1]
