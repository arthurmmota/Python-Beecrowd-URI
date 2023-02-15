countGenome = 0

while True:
    # (1 ≤ N ≤ 50000)
    N = int(input())
    if(N == 0):
        break
    else:
        genes = list(range(1,N+1))

        #(0 ≤ R ≤ 1000) inversões
        R = int(input())
        aux = 0
        for x in range(R):
            pares_genes  = list(int(entrada) for entrada in input().split())

            #print("pares_genes", pares_genes)
            subgenes = genes[pares_genes[0]-1:pares_genes[1]]

            #inverter
            subgenes.reverse()
            #print("Sub:", subgenes)
            genes[pares_genes[0]-1:pares_genes[1]] = subgenes

            #
            #print("Trocado", genes)
        #Q(0 ≤ Q ≤ 100) Colsutas
        Q = int(input())
        countGenome+=1
        print("Genome {0}".format(countGenome))

        for x in range(1,Q+1):
            consulta =  int(input())
            print(genes.index(consulta)+1)



