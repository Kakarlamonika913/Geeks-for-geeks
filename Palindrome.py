#User function Template for python3



class Solution:

    def isDigitSumPalindrome(self,N):

        newNum=0

        #calculating Digit Sum

        while(N>0):

            newNum+=N%10

            N//=10

        reversedNewNum=0

        N=newNum

        #reversing newNum

        while(N>0):

            reversedNewNum=reversedNewNum*10+N%10

            N//=10

        return 1 if reversedNewNum==newNum else 0  





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__=='__main__':

    t=int(input())

    for _ in range(t):

        N=int(input())

        ob=Solution()

        print(ob.isDigitSumPalindrome(N))

# } Driver Code Ends
