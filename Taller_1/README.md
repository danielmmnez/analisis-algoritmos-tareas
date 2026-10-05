# 1. Merge Intervals
Enlace: [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
Familia: Ordenamiento
Idea: Se ordena la lista de intervalos tomando como clave el extremo izquierdo (start). Luego se recorre la lista comparando si el inicio del intervalo actual es menor o igual al final del último intervalo guardado; si es así, se fusionan ensanchando el límite derecho (end), de lo contrario, se cierra el actual y se abre uno nuevo.
Complejidad: O(n)
Evidencia: ![Accepted — Merge Intervals](\Evidencias\merge-intervals-accepted.png)

# 2. Number of Islands
Enlace: [Number of Islands](https://leetcode.com/problems/number-of-islands/)
Familia: Grafos
Idea: La grilla actúa como un grafo implícito donde cada '1' es un vértice y sus vecinos ortogonales son las aristas. Se recorre la matriz y, cada vez que se encuentra un '1', se suma 1 al contador de islas y se lanza una búsqueda en profundidad (DFS) para hundir (marcar como '0') toda la componente conexa descubierta.
Complejidad: O(m \ n)
Evidencia: ![Accepted — Number of Islands](\Evidencias\number-of-islands-accepted.png)

# 3. Longest Common Subsequence
Enlace: [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
Familia: Programación Dinámica
Idea: Se construye una matriz dp[i][j] que representa la longitud de la subsecuencia más larga entre los prefijos de text1 (hasta i) y text2 (hasta j). Si los caracteres coinciden, el valor es 1 + dp[i-1][j-1]; si no coinciden, el valor se hereda del máximo entre ignorar un caracter del texto 1 o del texto 2 (max(dp[i-1][j], dp[i][j-1])).
Complejidad: O(n \ m)
Evidencia: ![Accepted — Longest Common Subsequence](\Evidencias\longest-common-subsequence-accepted.png)

# 4. Non-overlapping Intervals
Enlace: [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
Familia: Greedy
Idea: Para maximizar la cantidad de intervalos que caben (y por ende minimizar los borrados), el criterio greedy óptimo es ordenar los intervalos por su tiempo de finalización (end). Luego, se iteran aceptando el siguiente intervalo que empiece después o exactamente en el mismo instante en que terminó el último aceptado. Los omitidos se cuentan como borrados.
Complejidad: O(n)
Evidencia: ![Accepted — Non-overlapping Intervals](\Evidencias\non-overlapping-intervals-accepted.png)

# 5. Combination Sum
Enlace: [Combination Sum](https://leetcode.com/problems/combination-sum/)
Familia: Backtracking
Idea: Se utiliza una búsqueda recursiva donde el estado es el índice actual en los candidatos, el remanente por sumar y la combinación temporal. Se elige un candidato, se resta su valor del objetivo y se baja en el árbol recursivo (reutilizando el índice). Si la suma iguala el objetivo, se guarda la combinación; si lo supera, se poda la rama, y al retroceder se deshace la última elección (backtrack) para probar el siguiente número.
Complejidad: O(t/n)
Evidencia: ![Accepted — Combination Sum](\Evidencias\combination-sum-accepted.png)