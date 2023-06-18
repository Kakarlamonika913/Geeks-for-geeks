#User function Template for python3

class Solution:

        def EvenOddSum(self,N,Arr):

            EvenSum,OddSum=0,0

            for i in range(0,N,2):

                OddSum+=Arr[i]

            for i in range(1,N,2):

                EvenSum+=Arr[i]

            ans=[]

            ans.append(OddSum)

            ans.append(EvenSum)

            return ans

#{ 

 # Driver Code Starts

#Initial Template for Python 3

if __name__=='__main__':

    t=int(input())

    for _ in range(t):

        N=int(input())

        Arr=list(map(int,input().strip().split(' ')))

        ob=Solution()

        ans=ob.EvenOddSum(N,Arr)

        print(ans[0],end=" ")

        print(ans[1])

# } Driver Code Ends
