#User function Template for python3

class Solution:
	def find(self, A, B):
		# Code here
		dot = A[0]*B[0] + A[1]*B[1] + A[2]*B[2]

        cross = 0

        for i in range(3):

            cross+=A[i]*B[(i+1)%3]-A[(i+1)%3]*B[i]

        if cross == 0:

            return 1

        elif dot == 0:

            return 2

        else:

            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = list(map(int, input().split()))
		B = list(map(int,input().split()))
		ob = Solution()
		ans = ob.find(A, B)
		print(ans)
# } Driver Code Ends
