#User function Template for python3

class Solution:
	 def streamAvg(self, arr, n):
		 ans = []
		 average = 0
		 for i in range(n):
			 average += float(arr[i])
			 ans.append(float(average/(i+1)))
		 return ans;


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
