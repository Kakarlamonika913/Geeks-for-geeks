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



