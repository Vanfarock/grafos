import time
import queue
from texttable import Texttable

class Questao3:
  def __init__(self, caminho_arquivo):
    self.tempoExecucao = 0

    self.nos = []
    self.__carregar_arquivo(caminho_arquivo)

  def __carregar_arquivo(self, caminho_arquivo):
    file = open(caminho_arquivo, 'r')
    linhas = file.readlines()
    file.close()
    for i in range(0, int(linhas[0])):
      self.nos.append(No(i + 1))

    for line in linhas[1:]:
      relacao = [self.nos[int(i) - 1] for i in line.split()]
      relacao[0].adicionar(relacao[1])
      relacao[1].adicionar(relacao[0])

  def iniciar(self, numero_casos):
    self.__iniciar_dfs(numero_casos)
    self.__iniciar_bfs(numero_casos)

  def __iniciar_dfs(self, numero_casos):
    casos = []
    for _ in range(numero_casos):
      caso = CasoQuestao3(self.nos)
      caso.dfs()
      casos.append(caso)
      self.__shift(self.nos)
    self.__gerar_tabela('DFS', casos)

  def __iniciar_bfs(self, numero_casos):
    casos = []
    for _ in range(numero_casos):
      caso = CasoQuestao3(self.nos)
      caso.bfs()
      casos.append(caso)
      self.__shift(self.nos)
    self.__gerar_tabela('BFS', casos)

  def __shift(self, arr):
    primeiroValor = arr.pop(0)
    arr.append(primeiroValor)

  def __gerar_tabela(self, algoritmo, casos):
    header = [algoritmo]
    valores = ['Tempo medio execucao']
    
    tempoExecucaoTotal = 0
    t = Texttable(max_width=0)
    for i, caso in enumerate(casos):
      header.append(f'T{i + 1}')
      valores.append(formatarTempo(caso.tempoExecucao))
      tempoExecucaoTotal += caso.tempoExecucao

    header.append('Media')
    valores.append(formatarTempo(tempoExecucaoTotal / len(casos)))

    t.add_rows([header, valores])

    f = open("resultados_questao3.txt", "w")
    f.write(t.draw())
    f.close()

    print(t.draw())

def formatarTempo(segundos):
  return f'{round(segundos, 50)}s'


class CasoQuestao3:
  def __init__(self, nos):
    self.tempoExecucao = 0

    self.nos = nos

  def dfs(self):
    inicioTempoExecucao = time.time()
    for no in self.nos:
      if no.passou:
        continue
      self.__logica_dfs(no)

    fimTempoExecucao = time.time()
    self.tempoExecucao = fimTempoExecucao - inicioTempoExecucao
  
  def __logica_dfs(self, no):
    no.passou = True
    no.tempo += 1
    for filho in no.filhos:
      if filho.passou:
        continue

      filho.tempo = no.tempo
      filho.pai = no
      self.__logica_dfs(filho)

  def bfs(self):
    inicioTempoExecucao = time.time()
    
    fila = queue.Queue()
    fila.put(self.nos[0])
    while not fila.empty():
      u = fila.get()
      for filho in u.filhos:
        if filho.passou:
          continue

        fila.append(filho)
        filho.tempo = u.tempo + 1
        filho.pai = u
        filho.passou = True
      u.passou = True
    fimTempoExecucao = time.time()
    self.tempoExecucao = fimTempoExecucao - inicioTempoExecucao


class No:
  def __init__(self, id):
    self.id = id
    self.pai = None
    self.tempo = 0
    self.filhos = []
    self.passou = False

  def adicionar(self, outroNo):
    self.filhos.append(outroNo)

  def __str__(self):
    return f'Id: {self.id} - Tempo: {self.tempo}'