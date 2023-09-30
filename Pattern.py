#User function Template for python3
class Solution:
	def pattern(self, S):
		# code here
		i=len(S)
		ans=[]
		while i>=1:
		    ans.append(S[:i])
		    i-=1
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.pattern(S)
		for value in answer:
			print(value)
			

# } Driver Code Ends
