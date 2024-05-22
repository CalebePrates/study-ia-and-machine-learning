import mlrose_hiive

produtos = [
  ('Refrigerador A', 0.751, 999.9),
  ('Notebook A', 0.0035, 2499.9),
  ('Microondas C', 0.0319, 299.29),
  ('Notebook C', 0.527, 3999),
  ('Celular', 0.0000899, 2199.12),
  ('Ventilador', 0.496, 199.9),
  ('Refrigerador B', 0.635, 849),
  ('TV55', 0.4, 4346.99),
  ('TV50', 0.29, 3999.9),
  ('Microondas A', 0.0424, 308.66),
  ('Refrigerador C', 0.87, 1199.89),
  ('TV42', 0.2, 2999.9),
  ('Microondas B', 0.0544, 429.9),
  ('Notebook B', 0.498, 1999.9),
]

def imprimir_solucao(solucao):
  for i in range(len(solucao)):
    if solucao[i] == 1:
      print('%s - %s' % (produtos[i][0], produtos[i][2]))

def fitness_function(agenda):
  total_preco = 0
  capacidade_caminhao = 0
  for i in range(len(agenda)):
    if agenda[i] == 1:
      preco = produtos[i][2]
      capacidade = produtos[i][1]
      total_preco += preco
      capacidade_caminhao += capacidade
      if capacidade_caminhao > 3:
        total_preco = 1
    
  return total_preco

fitness = mlrose_hiive.CustomFitness(fitness_function)
problema = mlrose_hiive.DiscreteOpt(length=14, fitness_fn=fitness,
                              maximize = True, max_val = 2)
melhor_solucao, melhor_custo, _ = mlrose_hiive.hill_climb(problema)
imprimir_solucao(melhor_solucao)
print("LUCRO: ", melhor_custo)

melhor_solucao, melhor_custo, _ = mlrose_hiive.simulated_annealing(problema)
imprimir_solucao(melhor_solucao)
print("LUCRO: ", melhor_custo)

melhor_solucao, melhor_custo, _= mlrose_hiive.genetic_alg(problema, pop_size=500, mutation_prob=0.2)
imprimir_solucao(melhor_solucao)
print("LUCRO: ", melhor_custo)