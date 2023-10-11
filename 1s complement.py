#User function Template for python3
class Solution:
    def onesComplement(self,S,N):
        # code here
        ans=""
        
        for i in range(N):
           
            if(S[i] == '0'):
                ans = ans + '1'
           
            else:
                ans = ans + '0';
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.onesComplement(S,N))
# } Driver Code Ends
