from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[-1] * n for _ in range(m)]  
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            
            max_length = 1  # Pelo menos o próprio nó
            
            # Explorar todas as direções
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                # Verificar limites e se é crescente
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    max_length = max(max_length, 1 + dfs(ni, nj))
            
            memo[i][j] = max_length
            return max_length
        
        # Executar DFS a partir de cada célula
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result