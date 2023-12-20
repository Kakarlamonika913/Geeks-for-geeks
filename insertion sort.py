for i in range(1,n):
            key = alist[i]
            j=i-1
            while j>=0 and key<alist[j]:
                alist[j+1]=alist[j]
                j=j-1
            arr[j+1]=key    
          
