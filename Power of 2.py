#Back-end complete function Template for Python 3



class Solution:

    # Function to check if given number n is a power of two.

    def isPowerofTwo(self,n):

        if(n==0):

            return False

        

        #We use a counter variable to count number of set bits.

        count = 0

        while n>0:

            #Increment of counter variable if we get 1 as the rightmost bit.

            count+=(n&1)

            #Right Shift n to remove the rightmost bit.

            n>>=1

        #returning true if number of set bits is 1 otherwise false.

        return count==1;

        





#{ 

 # Driver Code Starts

#Initial Template for Python 3



import math





def main():

    

    T=int(input())

    

    while(T>0):

        

        

        n=int(input())

        ob=Solution()

        if ob.isPowerofTwo(n):

            print("YES")

        else:

            print("NO")

        

        T-=1



if __name__=="__main__":

    main()

# } Driver Code Ends
