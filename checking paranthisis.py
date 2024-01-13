  l=[]
        m=['(','[','{']
        
        for i in x:
            if i in m:
                l.append(i)
            elif i==')':
                if len(l)!=0 and l[-1]=='(':
                    l.pop()
                else:
                    return 0
            elif i==']':
                if len(l)!=0 and l[-1]=='[':
                    l.pop()
                else:
                    return 0
            elif i=='}':
                if len(l)!=0 and l[-1]=='{':
                    l.pop()
                else:
                    return 0
                
        if len(l)==0:
            return 1
        else:
            return 0
