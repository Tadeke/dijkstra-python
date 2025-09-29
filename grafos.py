import heapq as hp
from colorama import init, Fore, Style
from time import sleep


init()

def carregar_grafo(arquivo, direcionado=False):
    """
    Lê um grafo a partir de um arquivo texto.
    Formato esperado 
    origem destino peso       
        A B 2
        A C 5
        B C 1
        B D 3
        C D 2
    
    """
    grafo = {}
    with open(arquivo, "r") as f:
        for linha in f:
            if not linha.strip(): 
                continue
            origem, destino, peso = linha.strip().split()
            peso = float(peso)

            if origem not in grafo:
                grafo[origem] = []
            if destino not in grafo:
                grafo[destino] = []

            grafo[origem].append((destino, peso))
            if not direcionado: 
                grafo[destino].append((origem, peso))
    return grafo


def dijkstra(grafo, inicio, fim):
    
    #Busca de Custo Uniforme
    
    fila = [(0, inicio, [])]  # (custo acumulado, nó atual, caminho percorrido)
    visitados = set()

    while fila:
        (custo, no, caminho) = hp.heappop(fila)
        if no in visitados:
            continue

        caminho = caminho + [no]
        visitados.add(no)

        if no == fim:
            return custo, caminho

        for vizinho, peso in grafo.get(no, []):
            if vizinho not in visitados:
                hp.heappush(fila, (custo + peso, vizinho, caminho))

    return float("inf"), [] 


def main():

    while True:
        arquivo = input("digite o caminho do arquivo para leitura txt")
        print("Lendo arquivo\n")
        
        sleep(1)
        print("Arquivo lido \n\n")
        sleep(1)
        while True:
            print("==== Algoritmo de Dijkstra ====")
            arquivo = "grafo.txt"
            direcionado = False 

            grafo = carregar_grafo(arquivo, direcionado)

            origem = str(input("Informe o nó de origem: ")).upper().strip()
            destino = str(input("Informe o nó de destino: ")).upper().strip()

            custo, caminho = dijkstra(grafo, origem, destino)

            if caminho:
                print(Style.BRIGHT + f"\nMenor caminho de {origem} até {destino}: {' -> '.join(caminho)}")
                print(f"Custo total: {custo}")
            else:
                print(Fore.RED +"\nNão existe caminho entre os dois nós.")
            print(Style.RESET_ALL + '')

            deseja = input(str("deseja executar novamente o codigo")).upper().strip()[0]
            if deseja == "S":
                continue
            break

        deseja_2 = input(str("deseja executar novamente o codigo com outro txt ")).upper().strip()[0]
        if deseja_2 == "N":
            print(Fore.YELLOW + "fim do progama")
            break
            
            
main()

