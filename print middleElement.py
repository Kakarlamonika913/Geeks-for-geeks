class Solution:
    def middle(self,A,B,C):
        #code here
         if ((A>C) & (A<B)) | ((A<C) & (A>B)):
            return A
         elif ((B>C) & (B<A)) | ((B<C) & (B>A)):
              return B
         else:
             return C
