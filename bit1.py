 n = str(bin(N))
        cnt = 0
        
        for i in n:
            if i == '1':
                cnt+=1
        return cnt
