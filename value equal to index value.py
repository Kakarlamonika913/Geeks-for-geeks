#User function Template for python3
class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		out = []
        for i in range(n):
            if arr[i]==i+1:
                out.append(arr[i])
        return out
