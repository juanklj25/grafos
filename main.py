def circulo_euriliano(grafo):
    def remover(u, v):
        grafo[u].remove(v)
        grafo[v].remove(u)

    def encontrar_circuito(vertice_de_inicio):
        acumulador = [vertice_de_inicio]
        caminho = []
        while acumulador:
            u = acumulador[-1]
            if grafo[u]:
                v = grafo[u][0]
                acumulador.append(v)
                remover(u, v)
            else:
                caminho.append(acumulador.pop())
        return caminho

    for vertex in grafo:
        if len(grafo[vertex]) % 2 != 0:
            return None

    vertice_de_inicio = next(iter(grafo))
    circulo = encontrar_circuito(vertice_de_inicio)
    return circulo

grafo = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [0, 2]
}


circulo= circulo_euriliano(grafo)
if circulo:
    print("Circuito Euleriano encontrado:", circulo)
else:
    print("O grafo não é Euleriano")