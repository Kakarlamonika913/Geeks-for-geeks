#User function Template for python3



class Solution:

    def mulClock(self, num1, num2):

        

        pdt = num1*num2     # Product of the Numbers

        ans = pdt%12       # Remainder of the Product when divided by 12.

        

        return ans;





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__': 

    t = int (input ())

    for _ in range (t):

        num1,num2=map(int,input().split())

        

        ob = Solution()

        print(ob.mulClock(num1,num2))

# } Driver Code Ends
