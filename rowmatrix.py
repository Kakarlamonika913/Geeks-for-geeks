sol=[]
       flag=True
       for row in matrix:
           if flag:
               sol.extend(row)
               flag=False
           else:
                sol.extend(row[::-1])
                flag=True
       return sol
