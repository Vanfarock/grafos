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
      
      self.__gerar_tabela_dfs(i)
      casos.append(caso)
      self.__shift(self.nos)
      self.__reset(self.nos)
    
    self.__gerar_resultados('DFS', casos)

  def __iniciar_bfs(self, numero_casos):
    casos = []
    for i in range(numero_casos):
      caso = CasoQuestao3(self.nos)
      caso.bfs()
      self.__gerar_tabela_bfs(i)
    
      casos.append(caso)
      self.__shift(self.nos)
      self.__reset(self.nos)
    
    self.__gerar_resultados('BFS', casos)

  def __shift(self, arr):
    primeiroValor = arr.pop(0)
    arr.append(primeiroValor)

  def __reset(self, arr):
    for no in arr:
      no.pai = None
      no.tempo = 0
      no.tempo_fechamento = 0
      no.passou = False

  def __gerar_tabela_dfs(self, caso):
    f = open(Questao3.NOME_ARQUIVO_TABELAS, "a")
    caso += 1
    if caso == 1:
      f.write('=====================================================================\r\n')
      f.write(f'DFS\r\n')

    header = [f'T{caso}']
    d = ['d']
    pi = ['pi']

    for no in self.nos:
      header.append(no.id)
      d.append(f'{no.tempo}/{no.tempo_fechamento}')
      
      if no.pai is None: pi.append('null')
      else: pi.append(no.pai.id)

    t = Texttable(max_width=0)
    t.add_rows([header, d, pi])

    f = open(Questao3.NOME_ARQUIVO_TABELAS, "a")
    f.write(f'{t.draw()}\r\n')
    f.close()

  def __gerar_tabela_bfs(self, caso):
    f = open(Questao3.NOME_ARQUIVO_TABELAS, "a")
    caso += 1
    if caso == 1:
      f.write('=====================================================================\r\n')
      f.write(f'BFS\r\n')

    header = [f'T{caso}']
    d = ['d']
    pi = ['pi']

    for no in self.nos:
      header.append(no.id)
      d.append(no.tempo)
      
      if no.pai is None: pi.append('null')
      else: pi.append(no.pai.id)

    t = Texttable(max_width=0)
    t.add_rows([header, d, pi])

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
    self.tempo = 0

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
    self.tempo += 1
    no.tempo = self.tempo
    for filho in no.filhos:
      if filho.passou:
        continue

      filho.tempo = no.tempo
      filho.pai = no
      self.__logica_dfs(filho)
    
    self.tempo += 1
    no.tempo_fechamento = self.tempo

  def bfs(self):
    inicioTempoExecucao = time.time()
    
    fila = queue.Queue()
    fila.put(self.nos[0])
    while not fila.empty():
      u = fila.get()
      for filho in u.filhos:
        if filho.passou:
          continue

        fila.put(filho)
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
    self.tempo_fechamento = 0
    self.filhos = []
    self.passou = False

  def adicionar(self, outroNo):
    self.filhos.append(outroNo)

  def __str__(self):
    return f'Id: {self.id} - Tempo: {self.tempo}'