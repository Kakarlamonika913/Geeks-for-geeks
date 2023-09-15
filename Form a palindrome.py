#User function Template for python3



class Solution:

    def countMin(self, Str):

        # code here

        n = len(Str)

        

        #Creating a table to store the minimum number of palindromic cuts

        table = []

        

        #Initializing the table with 0

        for i in range(n):

            ro = [0]*n 

            table.append(ro)

            

        #Iterating over the string to fill the table

        for gap in range(1,n):

            

            #Setting the starting and ending indexes for each substring

            h = gap

            l = 0 

            

            while h<n:

                

                #Checking if the current substring is a palindrome

                if Str[l]==Str[h]:

                    table[l][h] = table[l+1][h-1]

                else:

                    #If not palindrome, calculating the minimum cuts required

                    table[l][h] = min(table[l][h-1], table[l+1][h]) + 1

                    

                #Updating the indexes

                l += 1 

                h += 1

                

        #Returning the minimum number of cuts required for the entire string  

        return table[0][-1];





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__':



    t = int(input())



    for _ in range(t):

        Str = input()

        



        solObj = Solution()



        print(solObj.countMin(Str))

# } Driver Code Ends
