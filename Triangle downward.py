#User function Template for python3



class Solution:

    def triDownwards(self, S):

        # code here

        ans=""

        for i in range(len(S)):

            for j in range(len(S)):

                if i>j:

                    ans+='.'

                else:

                    ans+=S[j]

        return ans

            





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__': 

    t = int (input ())

    for _ in range (t):

        

        S=input()

        

        ob = Solution()

        ans=ob.triDownwards(S)

        

        for i in range(len(ans)):

            print(ans[i],end="")

            if((i+1)%len(S))==0:

                print()

# } Driver Code Ends
