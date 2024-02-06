 adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj
