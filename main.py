class Grafos_estados:
    def __init__(self):
        self.estados = [
            "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
            "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
            "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí",
            "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
            "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
        ]
        self.num_estados = len(self.estados)
        self.matriz_adj = [[0] * self.num_estados for _ in range(self.num_estados)]

    def adicionar(self, estado1, estado2, distancia):
        index_estado1 = self.estados.index(estado1)
        index_estado2 = self.estados.index(estado2)
        self.matriz_adj[index_estado1][index_estado2] = distancia
        self.matriz_adj[index_estado2][index_estado1] = distancia

    def imprimir(self):

        for estado in self.estados:
            print(estado[:3].rjust(5), end="")
        print()
        for i in range(self.num_estados):
            print(self.estados[i][:3].rjust(3), end="")
            for j in range(self.num_estados):
                print(str(self.matriz_adj[i][j]).rjust(5), end="")
            print()

grafo_estados = Grafos_estados()

grafo_estados.adicionar("Paraíba", "Pernambuco", 259)
grafo_estados.adicionar("Pernambuco", "Piauí", 1126)
grafo_estados.adicionar("Piauí", "Tocantins", 2407)

grafo_estados.imprimir()
