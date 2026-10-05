from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # Límites o agua descubierta (o hundida)
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
            
            # Hundir la tierra visitada
            grid[r][c] = '0'
            
            # Recorrer vecinos ortogonales
            dfs(r - 1, c) # arriba
            dfs(r + 1, c) # abajo
            dfs(r, c - 1) # izquierda
            dfs(r, c + 1) # derecha
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
                    
        return islands