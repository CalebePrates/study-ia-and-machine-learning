class Vertice:
	def __init__(self, rotulo):
		self.rotulo = rotulo
		self.visitado = False
		self.adjacentes = []
	
	def adiciona_adjacente(self, adjacente):
		self.adjacentes.append(adjacente)

	def mostra_adjacentes(self):
		for i in self.adjacentes:
			print(i.vertice.rotulo, i.custo)