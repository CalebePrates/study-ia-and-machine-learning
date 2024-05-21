from algoritmos_busca.busca_gulosa.grafo import Grafo
from algoritmos_busca.busca_gulosa.gulosa import Gulosa
from algoritmos_busca.busca_gulosa.vetor_ordenado import VetorOrdenado

grafo = Grafo()
vetor = VetorOrdenado(5)

vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.imprime()

vetor.insere(grafo.lugoj)
vetor.imprime()

print('------------ Gulosa -----------')
busca_gulosa = Gulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.arad)