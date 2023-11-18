num_set=set(A)
    for index in range(1,N+1):
        if index not in num_set:
            return index
