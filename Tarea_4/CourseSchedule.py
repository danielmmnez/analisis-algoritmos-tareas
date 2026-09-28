# numCourses = 2, prerequisites = [[1,0]]

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # 1. Crear el grafo y el arreglo de grados de entrada (prerrequisitos pendientes)
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # 2. Construir el grafo dirigido
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        # 3. Encontrar todos los cursos que no tienen prerrequisitos
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                
        # 4. Procesar los cursos usando Búsqueda en Anchura (BFS)
        completed_courses = 0
        
        while queue:
            current = queue.popleft()
            completed_courses += 1
            
            # Al "completar" este curso, reducimos el requisito de sus vecinos
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                # Si un vecino ya no tiene prerrequisitos pendientes, lo añadimos a la cola
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 5. Si logramos completar la misma cantidad de cursos que numCourses, es posible
        return completed_courses == numCourses