#User function Template for python3

import math

class Solution:

    def cubeRoot(self, N):

        # code here 

        root = math.floor(N ** (1./3))

        return root





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__': 

    t = int (input ())

    for _ in range (t):

        N = int(input())

        

        ob = Solution()

        print(ob.cubeRoot(N))

# } Driver Code Ends
