#User function Template for python3



class Solution:

    def sumOfDigits(self, N):

        # code here

        sum1 = 0

        while(N>0):

            r=N%10

            sum1=sum1+r

            N=N//10

        return sum1





#{ 

 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__': 

    t = int (input ())

    for _ in range (t):

        N = int(input())

        ob = Solution()

        print(ob.sumOfDigits(N))

# } Driver Code Ends
