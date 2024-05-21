from algoritmos_busca.busca_aestrela.aestrela import AEstrela
from algoritmos_busca.busca_aestrela.grafo import Grafo

grafo = Grafo()
busca_aestrela = AEstrela(grafo.bucharest)
busca_aestrela.buscar(grafo.arad)