from questao2 import Questao2


def main():
    questao2 = Questao2()
    atual = questao2.iniciar()

    trace = []
    while atual != None:
        trace.append(atual)
        atual = atual.pai

    for step in trace[::-1]:
        print(step)


if __name__ == "__main__":
    main()
