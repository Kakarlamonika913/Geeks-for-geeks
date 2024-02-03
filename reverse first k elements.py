  size = len(q)
        arr = []

        for i in range(k):
            arr.append(q.popleft())
        for i in range(k):
            q.appendleft(arr[i])
            
        return q

