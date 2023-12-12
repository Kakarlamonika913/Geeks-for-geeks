dic = {}
        
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        for x in range(len(dic)):
            if dic[arr[x]]>1:
                return x+1   # return 1 based indexing
        return -1

