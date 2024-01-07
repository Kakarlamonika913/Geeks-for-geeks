  if n==0:
            return 0
        a=bin(n)
        s=a[:1]
        s=s+a[2:]
        s=s[::-1]
        for i in range(len(s)):
            if s[i]=='1':
                return i+1
