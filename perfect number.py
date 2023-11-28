 sum = 0
        for i in range(1,int(N**0.5)+1):
            if N%i == 0:
                sum = sum + (i + (N/i))
            else:
                sum += 0
        
        sum = int(sum/2)
        if sum == 1:
            sum = 0
        
        if sum == N:
            return 1
        else:
            return 0
