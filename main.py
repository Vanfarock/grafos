from graph import Graph

def main():
    graph = Graph(
      [[0, 1, 0],
       [1, 0, 1],
       [0, 1, 0]])
    print(graph)
    print(graph.getGraphEdgeType().name)
    print(graph.getEdgesCount())


if __name__ == "__main__":
    main()
