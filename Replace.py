#function should return an integer

#your task is to compplete this function

class Solution:

    def convertFive(self,n):

        #Code here

        num_str = str(n)

        updated_str = num_str.replace('0', '5')

        updated_num = int(updated_str)

        return updated_num

        

       

     





#{ 

 # Driver Code Starts

if __name__=='__main__':

    t = int(input())

    for i in range(t):

        n=int(input())

        print(Solution().convertFive(n))

# Contributed by: Harshit sidhwa



# } Driver Code Ends
