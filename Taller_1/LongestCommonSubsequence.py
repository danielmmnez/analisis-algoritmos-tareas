# text1 = "abcde", text2 = "ace" = 3
# text1 = "abcde", text2 = "ace" = 3
# text1 = "abc", text2 = "def" = 0

from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # Matriz dp con ceros por defecto (casos base)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    # Coincidencia: crece la subsecuencia
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # Diferencia: heredar el máximo de perder un lado u otro
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[n][m]