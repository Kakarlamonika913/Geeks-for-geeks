#User function Template for python3



class Solution:

    def splitString(ob, S): 

        # code here 

    

        result = [] 

        alpha = "" 

        num = "" 

        special = "" 

        

        

        for i in range(len(S)): 

        

            if((S[i] >= 'A' and S[i] <= 'Z') or

                (S[i] >= 'a' and S[i] <= 'z')): 

                alpha += S[i] 

            

        

            elif (S[i].isdigit()): 

                num = num+ S[i] 

            

            

            else: 

                special += S[i] 



     

        result.append(alpha) 

        result.append(num ) 

        result.append(special) 

        return result



       





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__':

    T = int(input())

    for _ in range(T):

        S = input()

        ob = Solution()

        ans = ob.splitString(S)

        for i in ans:

            if(i==""):

                print(-1)

            else:

                print(i)





# } Driver Code Ends
