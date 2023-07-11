#User function Template for python3

class Solution:
	def find_sum(self, n):
	    sum=(n*(n+1))/2
	    n=n//2
	    even=((2*n)+(n)*(n-1))
	    return [int(sum-even),int(even)]
	    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.find_sum(n)
		for _ in ans:
			print(_, end=" ")
		print()
# } Driver Code Ends
