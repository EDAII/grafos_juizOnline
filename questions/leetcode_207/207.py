from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        lista_adj = [[] for _ in range(numCourses)]
        
        grau_entrada = [0] * numCourses
        
        for curso, prereq in prerequisites:
            lista_adj[prereq].append(curso)
            grau_entrada[curso] += 1

        fila_processamento = deque()
        for disciplina in range(numCourses):
            if grau_entrada[disciplina] == 0:
                fila_processamento.append(disciplina)
        
        disciplinas_finalizadas = 0
        
        while fila_processamento:
            atual = fila_processamento.popleft()
            disciplinas_finalizadas += 1
            
            for dependente in lista_adj[atual]:
                grau_entrada[dependente] -= 1
                
                if grau_entrada[dependente] == 0:
                    fila_processamento.append(dependente)
        
        return disciplinas_finalizadas == numCourses