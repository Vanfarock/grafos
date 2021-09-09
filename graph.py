from enums import GraphEdgeType, GraphType

class Graph:
    def __init__(self, adjacencyMatrix):
        self.matrix = adjacencyMatrix

    def getGraphEdgeType(self):
      graphSize = len(self.matrix)
      for line in range(graphSize):
        for col in range(graphSize):
          if (self.matrix[line][col] != self.matrix[col][line]):
            return GraphEdgeType.DIRECTED
      return GraphEdgeType.UNDIRECTED

    def getGraphType(self):
      graphSize = len(self.matrix)
      for line in range(graphSize):
        for col in range(graphSize):
          if (self.matrix[line][line] > 0 or self.matrix[line][col] > 1):
            return GraphType.MULTIGRAPH
      return GraphType.SIMPLE

    def getGraphClass(self):
      pass

    def getEdgesCount(self):
      graphSize = len(self.matrix)
      degreesSum = sum([self.getVerticeDegree(i) for i in range(graphSize)])
      
      if (self.getGraphEdgeType() == GraphEdgeType.DIRECTED):
        return degreesSum
      return int(degreesSum / 2)

    def getVerticeDegree(self, index):
      return sum([1 for col in self.matrix[index] if col > 0])

    def __str__(self):
        string = ""
        for line in self.matrix:
            string += str(line)
            string += "\r\n"
        return string
