


def Knapsack(pontuacao, custo, dinheiro):

  n = len(pontuacao)
  if dinheiro <= 0 or n == 0 or len(custo) != n:
    return 0

  dp = [[0 for x in range(dinheiro+1)] for y in range(n)]


  for i in range(0, n):
    dp[i][0] = 0

 
  for c in range(0, dinheiro+1):
    if custo[0] <= c:
      dp[0][c] = pontuacao[0]
      
    

  for i in range(1, n):
    for c in range(1, dinheiro+1):
      pontuacao1, pontuacao2 = 0, 0

      if custo[i] <= c:
        pontuacao1 = pontuacao[i] + dp[i - 1][c - custo[i]]

      pontuacao2 = dp[i - 1][c]
     
      dp[i][c] = max(pontuacao1, pontuacao2)

  caminhoFinal=print_selected_elements(dp, custo, pontuacao, dinheiro)
  return (dp[n - 1][dinheiro], caminhoFinal)

def print_selected_elements(dp, custo, pontuacao, dinheiro):
  caminhoFinal = []
 
  n = len(custo)
  totalProfit = dp[n-1][dinheiro]
  for i in range(n-1, 0, -1):
    if totalProfit != dp[i - 1][dinheiro]:
      
      caminhoFinal.append(i)
      dinheiro -= custo[i]
      totalProfit -= pontuacao[i]

  if totalProfit != 0:
    caminhoFinal.append(0)
  return caminhoFinal

 
 




verdade2=True
arrayPontuacao=[]
arrayCusto=[]
arrayNome=[]
cont=0
contInput=0
dinheiroDisponivel=0
while verdade2==True:
    try:
        folha=input("")
        numero=""
        valor=folha.split(";")
        if ";" in folha:
            for i in valor:
                if i == ";":
                    pass
                else:
                    if cont == 0:
                        cont+=1
                        arrayNome.append(i)
                    elif cont ==1 :
                        arrayCusto.append(int(i))
                        cont+=1
                    elif cont == 2:
                        arrayPontuacao.append(int(i))
                        cont=0
       
        elif "parar" in folha :
            valorPrint=Knapsack(arrayPontuacao, arrayCusto, dinheiroDisponivel)
            print(valorPrint[0])
            contFinal=-1
            valorFinal=[]
            pontuacaoFinal=0
            caminhoFinal= valorPrint[1]
            for j in caminhoFinal:
                valorFinal.append(arrayNome[j])
                pontuacaoFinal += arrayCusto[j]
            valorFinal.reverse()
            print(pontuacaoFinal)
            for b in valorFinal:
                print(b)

        elif contInput==0:
            contInput=1
            dinheiroDisponivel= int(folha)  
        else:
            contInput=0    
     
    except EOFError:
        verdade2 = False
        break


