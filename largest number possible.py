 if(S==0 and N>1):
            return -1
        ans = ""
        for i in range(N):
            if S>=9:
                ans += "9"
                S -= 9
            else:
                ans += str(S)
                S -= S
        
        if(S>0):
            return -1
        else:
            return int(ans)
