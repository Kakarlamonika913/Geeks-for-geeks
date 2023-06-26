#User function Template for python3



#User function Template for python3

class Solution:

    def armstrongNumber (ob, n):

        # code here 

        k=n%100

        k1=k%10

        n1=n//100

        k2=k//10

        j=n1**3+k2**3+k1**3

        if j==n:

            return "Yes"

        else:

            return "No"





#{ 

 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__': 

    t = int (input ())

    for _ in range (t):

        n = input()

        n=int(n)

        ob = Solution()

        print(ob.armstrongNumber(n))

# } Driver Code Ends
