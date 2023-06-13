

#Back-end complete function Template for Python 3



class Solution:

    def check (self,s):

        ch = s[0]

        for i in range (1, len (s)):

            if s[i] != ch:

                return False

        return True

        

    # Contributed By: Pranay Bansal

#{ 

 # Driver Code Starts

#Initial Template for Python 3



t = int (input ())

for tc in range (t):

    s = input ()

    ob = Solution()

    if ob.check (s):

        print ("YES")

    else:

        print ("NO")

        

# Contributed By: Pranay Bansal



# } Driver Code Ends
