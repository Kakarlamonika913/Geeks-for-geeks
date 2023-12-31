total_sum = sum(A)
        
        left_sum = 0
        
        for i in range(N):
            left_sum += A[i]

            if ((total_sum - A[i]) //2) == left_sum - A[i]:
                    return i+1

        return -1
