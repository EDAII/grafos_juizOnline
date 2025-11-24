import heapq

class Solution:
    def minCost(self, maxTime, edges, passingFees):
        num_cidades = len(passingFees)
        
        grafo = [[] for _ in range(num_cidades)]
        for a, b, tempo in edges:
            grafo[a].append((b, tempo))
            grafo[b].append((a, tempo))

        INF = 10**18
        melhor = [[INF] * (maxTime + 1) for _ in range(num_cidades)]
        melhor[0][0] = passingFees[0]
        
        fila = [(passingFees[0], 0, 0)]
        
        while fila:
            custo_atual, tempo_atual, cidade_atual = heapq.heappop(fila)
            
            if custo_atual > melhor[cidade_atual][tempo_atual]:
                continue
            
            # Testar os vizinhos da cidade atual
            for vizinho, tempo_estrada in grafo[cidade_atual]:
                novo_tempo = tempo_atual + tempo_estrada
                if novo_tempo > maxTime:
                    continue
                
                novo_custo = custo_atual + passingFees[vizinho]
 
                if novo_custo < melhor[vizinho][novo_tempo]:
                    melhor[vizinho][novo_tempo] = novo_custo
                    heapq.heappush(fila, (novo_custo, novo_tempo, vizinho))
        
        resposta = min(melhor[num_cidades - 1])
        return resposta if resposta < INF else -1
