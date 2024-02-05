i = 0
j = 1
while j < len(A):
   if A[i] == A[j]:
       A.remove(A[j])
   elif A[i]<A[j]:
       i = i + 1
       j = j + 1
return len(A
