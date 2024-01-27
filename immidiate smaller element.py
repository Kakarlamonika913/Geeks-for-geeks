 visited = [False]*V
        visited[0] = True
        q = [0]
        result = []
        while q:
            temp = q.pop(0)
            if temp not in result:
                result.append(temp)
            for i in adj[temp]:
                if visited[i] == False:
                    visited[i] == True
                    q.append(i)
        return result

