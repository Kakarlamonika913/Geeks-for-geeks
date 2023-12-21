d={}
        for i in v1:
            d[i]=d.get(i,0)+1
        ans=[]
        for i in v2:
            if i in d:
                if d[i]!=0:
                    ans.append(i)
                    d[i]-=1
        return sorted(ans)
