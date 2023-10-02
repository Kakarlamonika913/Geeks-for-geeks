#User function Template for python3

class Solution:
	def find(self, l, b, h):
		# Code here
		sa=2*((l*b)+(b*h)+(l*h))
		vol=l*b*h
		return sa,vol
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		l, b, h = input().split()
		l = int(l); b = int(b); h = int(h);
		ob = Solution()
		ans = ob.find(l, b, h)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends
