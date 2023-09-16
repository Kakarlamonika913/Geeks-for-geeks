#User function Template for python3



class Solution:

    #Function to count number of ways to reach the nth stair.

    def countWays(self,n):

        

        # code here

        mod = 1000000007

        dp = [-1]*(n+5)

        

        #recursive function to solve the problem

        def solve(n,dp):

            #base case when n is 1 or 2

            if n<=2:

                dp[n] = n 

                return dp[n]

            

            #if the value is already calculated, return it

            if dp[n] != -1:

                return dp[n]

            

            #calculate the value using recursive calls and store it in dp

            dp[n] = (solve(n-1,dp)%mod + solve(n-2,dp)%mod) % mod

            return dp[n]

        

        #calling the solve function with input n and dp

        return solve(n,dp)





#{ 

 # Driver Code Starts

#Initial Template for Python 3

import atexit

import io

import sys

sys.setrecursionlimit(10**6)



# Contributed by : Nagendra Jha



if __name__ == '__main__':

    test_cases = int(input())

    for cases in range(test_cases):

        m = int(input())

        ob=Solution()

        print(ob.countWays(m))



# } Driver Code Ends
