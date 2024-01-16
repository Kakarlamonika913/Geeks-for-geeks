 s1=set(a)
        s2=set(b)
        missing=list(s1.difference(s2))
        return a.index(missing[0])
