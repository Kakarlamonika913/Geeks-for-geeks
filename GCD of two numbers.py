#User function Template for python3

class Solution:
    def gcd(self, A, B):
        # code here
        rem=1
        if A>B:
            dividend=A
            divisor=B
        else:
            dividend=B
            divisor=A
        while rem!=0:
            rem=dividend%divisor
            if rem!=0:
                dividend=divisor
                divisor=rem
        return divisor
       
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        A,B = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(A,B))
# } Driver Code Ends
