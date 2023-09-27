#User function Template for python3



class Solution:

    def count (self,s):

        # your code here

        res=[0 for i in range(4)]

        for i in s:

            if i>='A' and i<='Z':

                res[0]+=1

            elif i>='a' and i<='z':

                res[1]+=1

            elif i>='0' and i<='9':

                res[2]+=1

            else:

                res[3]+=1

        return res





#{ 

 # Driver Code Starts

#Initial Template for Python 3



t = int (input ())

for tc in range (t):

    s = input ()

    ob = Solution()

    res = ob.count (s)

    

    for i in res:

        print (i)

    

# Contributed By: Pranay Bansal



# } Driver Code Ends
