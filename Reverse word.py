#User function Template for python3



class Solution:

     def reverseWord(self, str: str) -> str:

        #your code here

        rev = ""

        for i in range(len(str)-1, -1, -1):

            rev += str[i]

        return rev





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == "__main__":

    t = int(input())

    while(t>0):

        s = input()

        ob = Solution()

        print(ob.reverseWord(s))

        t = t-1



# } Driver Code Ends
