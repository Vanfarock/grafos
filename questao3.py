import time
import queue
from texttable import Texttable

class Questao3:
  NOME_ARQUIVO_RESULTADOS = "resultados_questao3.txt"
  NOME_ARQUIVO_TABELAS = "tabelas_questao3.txt"

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
    self.__limpar_arquivo(Questao3.NOME_ARQUIVO_RESULTADOS)
    self.__limpar_arquivo(Questao3.NOME_ARQUIVO_TABELAS)

    self.__iniciar_dfs(numero_casos)
    self.__iniciar_bfs(numero_casos)

  def __limpar_arquivo(self, nome_arquivo):
    f = open(nome_arquivo, "w")
    f.write("")

  def __iniciar_dfs(self, numero_casos):
    casos = []
    for i in range(numero_casos):
      caso = CasoQuestao3(self.nos)
      caso.dfs()
      self.__gerar_tabela("DFS", i)
      casos.append(caso)
      self.__shift(self.nos)
    self.__gerar_resultados('DFS', casos)

  def __iniciar_bfs(self, numero_casos):
    casos = []
    for i in range(numero_casos):
      caso = CasoQuestao3(self.nos)
      caso.bfs()
      self.__gerar_tabela("BFS", i)
      casos.append(caso)
      self.__shift(self.nos)
    self.__gerar_resultados('BFS', casos)

  def __shift(self, arr):
    primeiroValor = arr.pop(0)
    arr.append(primeiroValor)

  def __gerar_tabela(self, algoritmo, caso):
    f = open(Questao3.NOME_ARQUIVO_TABELAS, "a")
    caso += 1
    if caso == 1:
      f.write('=====================================================================\r\n')
      f.write(f'{algoritmo}\r\n')

    header = [f'T{caso}']
    pi = ['Pi']
    pai = ['Pai']

    for no in self.nos:
      header.append(no.id)
      pi.append(no.tempo)
      
      if no.pai is None: pai.append('null')
      else: pai.append(no.pai.id)

    t = Texttable(max_width=0)
    t.add_rows([header, pi, pai])

    f = open(Questao3.NOME_ARQUIVO_TABELAS, "a")
    f.write(f'{t.draw()}\r\n')
    f.close()

  def __gerar_resultados(self, algoritmo, casos):
    header = [algoritmo]
    valores = ['Tempo medio execucao']
    
    tempoExecucaoTotal = 0
    for i, caso in enumerate(casos):
      header.append(f'T{i + 1}')
      valores.append(formatarTempo(caso.tempoExecucao))
      tempoExecucaoTotal += caso.tempoExecucao

    header.append('Media')
    valores.append(formatarTempo(tempoExecucaoTotal / len(casos)))

    t = Texttable(max_width=0)
    t.add_rows([header, valores])

    f = open(Questao3.NOME_ARQUIVO_RESULTADOS, "a")
    f.write(f'{t.draw()}\r\n')
    f.close()

def formatarTempo(segundos):
  return f'{round(segundos, 2)}s'


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