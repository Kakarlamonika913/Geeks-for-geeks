max0 = A[0]
        min0 = A[0]
        for i in range(1,N):
          if A[i] > max0:
              max0 = A[i]

          if A[i] < min0:
              min0 = A[i]

        res = min0 + max0
        return res
