#User function Template for python3



class Solution:

    def findIndex (self,a, N, key ):

        #code here.

        b=[]

        if key not in a:

            return -1,-1

        for i in range(N):

            if a[i]==key:

                b.append(i)

        return min(b),max(b)





#{ 

 # Driver Code Starts

#Initial Template for Python 3





t=int(input())

for _ in range(0,t):

    n=int(input())

    a=list(map(int,input().split()))

    key=int(input())

    ob = Solution()

    ans=ob.findIndex(a, n, key )

    print(*ans)

    

# } Driver Code Ends
