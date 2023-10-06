#User function Template for python3

class Solution:



	def fascinating(self,n):

	    # code here

	    a=str(n)

	    num=str(n*3)

	    num1=str(n*2)

	    b=a+num+num1

	    lst=[]

	    lst[:0]=b

	    lst.sort()

	    lst1=['1','2','3','4','5','6','7','8','9']

        if(lst==lst1):

            return True

        else:

            return False 



#{ 

 # Driver Code Starts

#Initial Template for Python 3







if __name__ == '__main__':

    tc = int(input())

    while tc > 0:

        n = int(input().strip())

        ob = Solution()

        ans = ob.fascinating(n)

        if ans:

            print("Fascinating")

        else:

            print("Not Fascinating")

        tc -= 1



# } Driver Code Ends
