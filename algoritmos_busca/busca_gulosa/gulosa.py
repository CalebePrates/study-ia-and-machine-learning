from .vetor_ordenado import VetorOrdenado
from .vertice import Vertice

class Gulosa:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual: Vertice):
    print('---------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado = True
          vetor_ordenado.insere(adjacente.vertice)
      vetor_ordenado.imprime()

      if len(vetor_ordenado.valores) != 0:
        self.buscar(vetor_ordenado.valores[0])