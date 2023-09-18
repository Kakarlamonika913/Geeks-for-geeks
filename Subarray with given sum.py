

class Solution:

    def subArraySum(self,arr, n, sum_): 

        A = []

        curr_sum = arr[0]

        start = 0

        i = 1

        while i <= n:

            while curr_sum > sum_ and start < i-1:

        

                curr_sum = curr_sum - arr[start]

                start +=1

            if curr_sum == sum_:

                A.append(start+1)

                A.append(i)

                return A



            # Add this element 

            # to curr_sum

            if i < n:

                curr_sum = curr_sum + arr[i]

            i += 1



        # If we reach here, 

        # then no subarray

        A.append(-1)

        return A





#{ 

 # Driver Code Starts

#Initial Template for Python 3



import math



def main():

        T=int(input())

        while(T>0):

            

            NS=input().strip().split()

            N=int(NS[0])

            S=int(NS[1])

            

            A=list(map(int,input().split()))

            ob=Solution()

            ans=ob.subArraySum(A, N, S)

            

            for i in ans:

                print(i, end=" ")

                

            print()

            

            T-=1





if __name__ == "__main__":

    main()

# } Driver Code Ends
