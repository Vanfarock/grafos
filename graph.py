class Node:
    def __init__(self, value):
        self.value = value
        self.siblings = []

    def addSibling(self, node):
        self.siblings.append(node)


class Graph:
    def __init__(self, adjacencyMatrix):
        self.matrix = adjacencyMatrix
        self.nodes = self.__initNodes()

    def __initNodes(self) -> list[Node]:
        nodes = [Node(i) for i in range(len(self.matrix))]
        for i, line in enumerate(self.matrix):
            for j, col in enumerate(line):
                if (col == 1):
                    nodes[i].addSibling(nodes[j])
        return nodes

    def showNodes(self):
        message = ""
        for node in self.nodes:
            message += f"{node.value} - {[sibling.value for sibling in node.siblings]}"
            message += "\r\n"
        return message

    def __str__(self):
        string = ""
        for line in self.matrix:
            string += str(line)
            string += "\r\n"
        return string
