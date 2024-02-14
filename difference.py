  mp={}
        
        for i in arr:
            if(abs(i-N) in mp or i+N in mp):
                return True
            mp[i]=1
                    
        return False
