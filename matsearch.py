r=0
        c=M-1
        while r<N and c>=0:
            if mat[r][c]==X:
                return 1
            elif mat[r][c]>x:
                c-=1
            else:
                r+=1
        return 0
