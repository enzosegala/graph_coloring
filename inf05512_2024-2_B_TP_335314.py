## trablho final análise combinatória e grafos Enzo Borges Segala 00335314


import os


def read_all_txt_files(file): ## leitor de arquivo
    # txt_files = [f for f in os.listdir() if f.endswith(".txt")]
    if not file:
        print("No .txt files found in the current directory.")
        return

    
    print(f"Reading file: {file}")
    with open(file, "r") as f:
        # Read the first line
        first_line = f.readline().strip()  # Read and strip extra whitespace
        # arestas = f.read().strip()
        arestas = f.readlines()
        # print(arestas)
        return first_line,arestas

def menor_numero(arr): ## para o algotimo utilizo essa funcao para determinar o menor valor(cor) possível inteiro positivo
    if arr ==[]:
        return  1
    arr = sorted(arr)
    smallest = 1 
    for num in arr:
        if num == smallest:
            smallest += 1
    return smallest


class Graph: ## criando a classe grafo 
    def __init__(self):
        self.num_nos = 0
        self.num_arestas= 0
        self.graph = {}
        self.list_nodos={}
        self.list_visitados=[]
        

    
    def assign_first_line(self,first_line): ## leitura da primeira linha 
        numbers = [int(num) for num in first_line.split() if num.isdigit()]
        self.num_nos=numbers[0]
        self.num_arestas=numbers[1]
        # print(self.num_nos,self.num_arestas)

    def add_aresta(self, orig, destino): ## adiciona arestas (funcao interna)
        if orig != destino:
            if orig not in self.graph:
                self.graph[orig] = []
            self.graph[orig].append(destino)

            if destino not in self.graph:
                self.graph[destino] = []
            self.graph[destino].append(orig)
    
    def assing_arestas(self,arestas): ##  para cada linha adiciona a areasta correspondente 
        for line in arestas:
            numbers = [int(num) for num in line.split() if num.isdigit()]
            
            self.add_aresta(numbers[0],numbers[1])
        
    


    def color(self,nodo): ## algoritmo de coloracao em si: trata o primeiro caso depois trara para nodos que foram visitados
        # que seja conectados ao nodo do grafo adiciona a uma lista as cores desses nodos e busca-se a menor cor possível.
        # a funcao recebe o nodo na ordem inversa da que o sort do grafos (em numero de nodos conectados)
        lista_intermediaria=[]
        if self.list_visitados == []:
            self.list_nodos[nodo]= 1 
        else:
            for nodos_antecedentes in self.list_visitados:
                    if nodos_antecedentes in self.graph[nodo]:
                        lista_intermediaria.append(self.list_nodos[nodos_antecedentes])              
        
        self.list_nodos[nodo] = menor_numero(lista_intermediaria)
        # print(lista_intermediaria,menor_numero(lista_intermediaria),nodo)        
        

        

    def coloring_algorithm(self): ## funcao que chama a coloracao e passa cada nodo na ordem de menos nodos para mais nodos conectados 
        copy_graph=self.graph.copy()
        
        nos_ordenados = list((sorted(copy_graph.items(), key=lambda item: len(item[1]))))
        print(nos_ordenados)
        while nos_ordenados:
            nodo = nos_ordenados.pop(0)[0] 
            copy_graph.pop(nodo) 
            self.color(nodo)
            self.list_visitados.append(nodo)
            nos_ordenados =list((sorted(copy_graph.items(), key=lambda item: len(item[1]))))


    def print_nodes(self):
        self.list_nodos=sorted(self.list_nodos.items())
        print((self.list_nodos))
    
    def export_table(self,input_name):
        filename = f"{input_name}.color"

        with open(filename, 'w') as file:
            # for item in self.list_nodos:
            #     file.write(f"{item}\n")
            for tup in self.list_nodos:
                file.write(" ".join(map(str, tup)) + "\n")
        

        


if __name__ == "__main__":
    txt_files = [f for f in os.listdir() if f.endswith(".txt")]
    for file in txt_files:
        print(txt_files)
        first_line,arestas =read_all_txt_files(file)
        graph= Graph()
        graph.assign_first_line(first_line)
        graph.assing_arestas(arestas)
        graph.coloring_algorithm()
        graph.print_nodes()
        graph.export_table(file)

