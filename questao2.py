class Questao2:
  def __init__(self):

    self.nos = [
      [No(9),  No(8),    No(7),    No(6), No(5),    No(4),    No(3)],
      [No(10), No(9),    No(8),    No(7), No(None), No(None), No(2)],
      [No(11), No(None), No(None), No(8), No(None), No(0),    No(1)],
      [No(12), No(11),   No(10),   No(9), No(None), No(1),    No(2)],
      [No(11), No(None), No(None), No(8), No(None), No(None), No(3)],
      [No(10), No(9),    No(8),    No(7), No(7),    No(5),    No(4)],
      [No(11), No(None), No(None), No(8), No(6),    No(6),    No(5)],
    ]
    
    for lin in range(len(self.nos)):
      for col in range(len(self.nos)):
        self.nos[lin][col].posicao = (lin, col)

    self.inicio = self.nos[6][0]
    self.destino = self.nos[2][5]

  def iniciar(self):
    aberto = [self.inicio]
    fechado = []
    self.inicio.funcao = 0

    while len(aberto) > 0:
      atual = self.menor_aberto(aberto)
      aberto.remove(atual)
      fechado.append(atual)

      if atual == self.destino:
        return atual

      for noAdjacente in self.obter_nos_adjacentes(atual):
        if noAdjacente.eh_obstaculo():
          continue

        if noAdjacente in fechado:
          continue

        noAdjacente.pai = atual
        noAdjacente.distancia = atual.distancia + 1
        noAdjacente.funcao = noAdjacente.distancia + noAdjacente.heuristica

        if noAdjacente in aberto:
          continue

        aberto.append(noAdjacente)
    return None

  def menor_aberto(self, aberto):
    return min(aberto, key=lambda no: no.funcao)

  def obter_nos_adjacentes(self, atual):
    n = len(self.nos)
    direcoes = [
      [1, 0],
      [0, 1],
      [-1, 0],
      [0, -1],
    ]

    movimentos = []
    for direcao in direcoes:
      dx = atual.posicao[0] + direcao[0]
      dy = atual.posicao[1] + direcao[1]
      if dx >= 0 and dx < n and dy >= 0 and dy < n:
        movimentos.append(self.nos[dx][dy])
    return movimentos

  def mostrar_caminho(self, destino):
    atual = destino
    trace = []
    while atual != None:
        trace.append(atual)
        atual = atual.pai

    for step in trace[::-1]:
        print(step)

    if len(trace) == 0:
        print('Não existe caminho possível')

class No:
  def __init__(self, heuristica):
    self.heuristica = heuristica
    
    self.posicao = (None, None)
    self.pai = None
    self.distancia = 0
    self.funcao = 0

  def eh_obstaculo(self):
    return self.heuristica == None

  def __str__(self):
    return f'{self.posicao} - {self.heuristica}'
