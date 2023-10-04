#User function Template for python3
class Solution:
	def numberPattern(self, N):
		# code here
		disp=[]
		for i in range(1,N+1):
		    new=[]
		    for j in range(1,i+1):
		        new.append(str(j))
		    disp.append("".join(new+new[-2::-1]))
		return disp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        res = ob.numberPattern(N)
        for each in res:
            print(each, end=" ")
        print()
        

# } Driver Code Ends
