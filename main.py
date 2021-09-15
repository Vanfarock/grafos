from graph import Graph

def tipoDoGrafo():
    pass

def ehDirigido(matriz):
      n = len(matriz)
      for lin in range(n):
        for col in range(n):
          if (matriz[lin][col] != matriz[col][lin]):
            return True
      return False

def ehSimples(matriz):
    n = len(matriz)
    for lin in range(n):
        for col in range(n):
            if (matriz[lin][lin] > 0 or matriz[lin][col] > 1):
                return False
    return True

def ehRegular(matriz):
    n = len(matriz)
    for lin in range(n):
        pass

def getGrauVerticeLinha(matriz, indice):
    return sum([2 if i == indice else 1 for i, col in enumerate(matriz[indice]) if col > 0])

def getGrauVerticeColuna(matriz, indice):
    return sum([lin[indice] for lin in matriz if lin[indice] > 0])

def grausDoVertice(matriz):
    if (ehDirigido(matriz)):
        return grausDoVerticeDigrafo(matriz)
    return grausDoVerticeGrafo(matriz)

def grausDoVerticeDigrafo(matriz):
    grausEntrada = {}
    grausSaida = {}

    n = len(matriz)
    for i in range(n):
        grausEntrada[i] = getGrauVerticeColuna(matriz, i)
        grausSaida[i] = getGrauVerticeLinha(matriz, i)
    
    retorno = f"Sequencia de graus de entrada: {', '.join(getSequenciaGraus(grausEntrada))}\r\n"
    retorno += f"Sequencia de graus de saida: {', '.join(getSequenciaGraus(grausSaida))}\r\n"
    retorno += f"Grau de entrada de cada vertice:\r\n"
    retorno += "\r\n".join(getListaGraus(grausEntrada))
    retorno += f"\r\nGrau de saida de cada vertice:\r\n"
    retorno += "\r\n".join(getListaGraus(grausSaida))
    
    return retorno

def grausDoVerticeGrafo(matriz):
    graus = {}

    n = len(matriz)
    for lin in range(n):
        graus[lin] = getGrauVerticeLinha(matriz, lin)
    
    retorno = f"Sequencia de graus: {', '.join(getSequenciaGraus(graus))}\r\n"

    retorno += "Grau de cada vertice:\r\n"
    retorno += "\r\n".join(getListaGraus(graus))
    
    return retorno

def getSequenciaGraus(graus):
    grausOrdenados = sorted(graus.items(), key=lambda item : item[1])
    return [str(v) for _, v in grausOrdenados]

def getListaGraus(graus):
    return [f"{k} - {v}" for k, v in graus.items()]

def arestasDoGrafo(matriz):
    n = len(matriz)
    somaGraus = sum([getGrauVerticeLinha(matriz, i) for i in range(n)])
    
    if (ehDirigido(matriz)):
        return arestasDoGrafoDirigido(matriz, somaGraus)
    return arestasDoGrafoNaoDirigido(matriz, int(somaGraus / 2))

def arestasDoGrafoDirigido(matriz, quantidadeArestas):
    retorno = f"Quantidade de arestas: {quantidadeArestas}\r\n"
    retorno += "Conjunto de arestas:\r\n"
    
    retorno += 


def arestasDoGrafoNaoDirigido(matriz, quantidadeArestas):
    pass

def main():
    matriz = [[0, 1, 0, 1],
              [1, 0, 1, 1],
              [0, 1, 0, 1],
              [1, 1, 1, 0]]

    print(grausDoVertice(matriz))
    print(arestasDoGrafo(matriz))
    # graph = Graph(
    #   [[0, 1, 0],
    #    [1, 0, 1],
    #    [0, 1, 0]])
    # print(graph)
    # print(graph.getGraphEdgeType().name)
    # print(graph.getEdgesCount())


if __name__ == "__main__":
    main()
