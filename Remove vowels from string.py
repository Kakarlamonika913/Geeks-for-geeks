#User function Template for python3

class Solution:

	def removeVowels(self, S):

		# code here

		S1='aeiouAEIOU'

		l1=[]

		for i in S:

		    if i not in S1:

		        l1.append(i)

		return "".join(l1)

		





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__':

	T=int(input())

	for i in range(T):

		s = input()

		

		ob = Solution()	

		answer = ob.removeVowels(s)

		

		print(answer)





# } Driver Code Ends
