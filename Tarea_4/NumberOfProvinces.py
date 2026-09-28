[[1,1,0],[1,1,0],[0,0,1]]

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        # Función auxiliar para recorrer todas las ciudades de una misma provincia
        def dfs(city):
            for neighbor in range(n):
                # Si hay conexión directa y el vecino no ha sido visitado
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    
        # Recorremos cada ciudad
        for i in range(n):
            if i not in visited:
                # Encontramos una nueva ciudad no visitada, es decir, una nueva provincia
                provinces += 1
                visited.add(i)
                dfs(i) # Marcamos todas las ciudades conectadas a esta
                
        return provinces