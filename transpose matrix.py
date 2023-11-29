 for i in range(n):
            for j in range(i + 1, n):
                # Swap elements at (i, j) and (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
