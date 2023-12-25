 a=[None]*n
        for i in range(n):
            a[i]=arr[i]
        arr.sort()
        for i in range(n):
            if(a[i]!=arr[i]):
                return 0
        return 1
