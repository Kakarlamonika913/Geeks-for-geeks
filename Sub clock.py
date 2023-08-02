#User function Template for python3



class Solution:

    def subClock(self, num1, num2):

        # code here

        ans = num1-num2    # Subtracting num2 from num1

        ans %= 12

        if(ans<0):

            ans+=12

        

        return ans





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__': 

    t = int (input ())

    for _ in range (t):

        num1,num2=map(int,input().split())

        

        ob = Solution()

        print(ob.subClock(num1,num2))

# } Driver Code Ends
