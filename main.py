import sys
from questao2 import Questao2
from questao3 import CasoQuestao3, Questao3

def main():
  sys.setrecursionlimit(10000)
  
  # questao2 = Questao2()
  # destino = questao2.iniciar()
  # questao2.mostrar_caminho(destino)
  
  questao3 = Questao3('test3.txt')
  questao3.iniciar(1)

if __name__ == '__main__':
  main()
