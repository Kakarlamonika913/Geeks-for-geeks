def printPat(n):

    #Code here

    m=n

    for i in range(n,0,-1):

        for j in range(n,0,-1):

            print((str(j)+" ")*m,end="")

        m-=1

        print("$",end="")

    print()





#{ 

 # Driver Code Starts

if __name__=='__main__':

    t=int(input())

    for i in range(t):

        n= int(input())

        printPat(n)

# } Driver Code Ends
