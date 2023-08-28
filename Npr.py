#User function Template for python3

class Solution:
    def nPr(self, n, r):
        # code here
        def fact(num):
            if num==0:
                return 1
            else:
                return num*(fact(num-1))
        return int((fact(n))/fact(n-r))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
# } Driver Code Ends
