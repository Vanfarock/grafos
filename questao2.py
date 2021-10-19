import math

class Questao2:
  def __init__(self):
    self.inicio = (6, 0)
    self.destino = (2, 5)

    inf = math.inf
    self.heuristica = [
      [9 ,   8 ,  7  , 6,   5 ,   4 , 3],
      [10,   9 ,  8  , 7, None, None, 2],
      [11, None, None, 8, None,   0 , 1],
      [12,  11 ,  10 , 9, None,   1 , 2],
      [11, None, None, 8, None, None, 3],
      [10,   9 ,   8 , 7,   6 ,   5 , 4],
      [11, None, None, 8,   7 ,   6 , 5],
    ]

    self.funcao = {}

  def iniciar(self):
    tempo = 0
    aberto = {self.inicio}
    fechado = {}
    self.funcao[self.inicio] = 0

    while len(aberto) > 0:
      atual = self.menor_aberto(aberto)
      aberto.remove(atual)
      fechado.append(atual)

      if atual == self.destino:
        return fechado

      

    pass

  # def acessar(self, matriz, coordenada):
  #   return matriz[coordenada[0]][coordenada[1]]

  # def settar(self, matriz, coordenada, valor):
  #   matriz[coordenada[0]][coordenada[1]] = valor

  # def menor_aberto(self, aberto):
  #   return min(aberto, key=lambda no: self.funcao[no[0]][no[1]])

  # def obter_movimentacoes(self, atual, fechado):
  #   n = len(self.heuristica)
  #   direcoes = [
  #     [1, 0],
  #     [0, 1],
  #     [-1, 0],
  #     [0, -1],
  #   ]

  #   for direcao in range(direcoes):
  #     dx = atual[0] + direcao[0]
  #     dy = atual[1] + direcao[1]
  #     if dx >= 0 and dx < n and dy >= 0 and dy < n and direcoes.c
