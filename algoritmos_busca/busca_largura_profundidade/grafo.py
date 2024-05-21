from .vertice import Vertice
from .adjacente import Adjacente

class Grafo:
	arad = Vertice('Arad')
	zerind = Vertice('Zerind')
	oradea = Vertice('Oradea')
	sibiu = Vertice('Sibiu')
	timisoara = Vertice('Timisoara')
	lugoj = Vertice('Lugoj')
	mehadia = Vertice('Mehadia')
	dobreta = Vertice('Dobreta')
	craiova = Vertice('Craiova')
	rimnicu = Vertice('Rimnicu')
	fagaras = Vertice('Fagaras')
	pitesti = Vertice('Pitesti')
	bucharest = Vertice('Bucharest')
	giurgiu = Vertice('Giurgiu')

	arad.adiciona_adjacente(Adjacente(zerind, 75))
	arad.adiciona_adjacente(Adjacente(sibiu, 140))
	arad.adiciona_adjacente(Adjacente(timisoara, 118))

	zerind.adiciona_adjacente(Adjacente(arad, 75))
	zerind.adiciona_adjacente(Adjacente(oradea, 71))

	oradea.adiciona_adjacente(Adjacente(zerind, 71))
	oradea.adiciona_adjacente(Adjacente(sibiu, 151))

	sibiu.adiciona_adjacente(Adjacente(oradea, 151))
	sibiu.adiciona_adjacente(Adjacente(arad, 140))
	sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
	sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

	timisoara.adiciona_adjacente(Adjacente(arad, 118))
	timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

	lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
	lugoj.adiciona_adjacente(Adjacente(mehadia, 70))
 
	mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
	mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

	dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
	dobreta.adiciona_adjacente(Adjacente(craiova, 120))