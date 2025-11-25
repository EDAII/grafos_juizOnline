class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        rank = {}
        
        # Inicializar Union-Find para todas as letras
        for eq in equations:
            a, b = eq[0], eq[3]
            if a not in parent:
                parent[a] = a
                rank[a] = 0
            if b not in parent:
                parent[b] = b
                rank[b] = 0
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                if rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                elif rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        # Primeira fase: processar igualdades
        for eq in equations:
            if eq[1] == '=':
                a, b = eq[0], eq[3]
                union(a, b)
        
        # Segunda fase: verificar desigualdades
        for eq in equations:
            if eq[1] == '!':
                a, b = eq[0], eq[3]
                if find(a) == find(b):
                    return False
        
        return True