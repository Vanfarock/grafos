class Questao3:
  def __init__(self, caminho_arquivo):
    file = open(caminho_arquivo, 'r')

    self.nos = []
    linhas = file.readlines()
    for i in range(0, int(linhas[0])):
      self.nos.append(No(i + 1))

    for line in linhas[1:]:
      relacao = [self.nos[int(i) - 1] for i in line.split()]
      relacao[0].adicionar(relacao[1])
      relacao[1].adicionar(relacao[0])

  def iniciar(self):
    pass

class No:
  def __init__(self, id):
    self.id = id
    self.arestas = []

  def adicionar(self, outroNo):
    self.arestas.append(outroNo)

  def __str__(self):
    return f'Id: {self.id} - Grau: {len(self.arestas)}'