from enum import Enum

class GraphEdgeType(Enum):
  UNDIRECTED = 0
  DIRECTED = 1

class GraphType(Enum):
  SIMPLE = 0
  MULTIGRAPH = 1

class GraphClass(Enum): 
  REGULAR = 0
  COMPLETE = 1
  NULL = 2
