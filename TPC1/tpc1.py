#TPC 1 - A96159

N_LINE_ELEMS = 6
doentesPorEscalaoEtario = {}
doentesPorNivelColesterol = {}
distribuicaoPorEscEtario = {}
distribuicaoNivelCol = {}
totalDoentesFemininos = 0
totalDoentesMasculinos = 0
limSuperiorIdade = 0
limInferiorIdade = 0
limSuperiorColesterol = 0
limInferiorColesterol = 0


def readfile(fullFileName):

    global totalDoentesFemininos
    global totalDoentesMasculinos
    global limSuperiorIdade
    global limInferiorIdade
    global limSuperiorColesterol
    global limInferiorColesterol

    global doentesPorEscalaoEtario
    global doentesPorNivelColesterol

    f = open(fullFileName, "r")
    
    if(f!=None):
        buffer = f.readline()                                   #TÍTULO 
        if(buffer != ""):
            buffer = f.readline()                               #1ª linha de dados
            nLinesLidasComDoenca = 0
            while(buffer != ""):
                size = len(buffer) - 1
                itens = (buffer[:size]).split(",")
                if(len(itens) == N_LINE_ELEMS):
                    temDoenca = int(itens[5])
                    if(temDoenca == 1):
                        nLinesLidasComDoenca = nLinesLidasComDoenca + 1
                        idade = int(itens[0])
                        sexo = itens[1]
                        colesterol = int(itens[3])
                        if(nLinesLidasComDoenca == 1):
                            limInferiorIdade = idade
                            limSuperiorIdade = idade
                            limInferiorColesterol = colesterol
                            limSuperiorColesterol = colesterol
                        else:
                            if(idade > limSuperiorIdade):
                                limSuperiorIdade = idade
                            if(idade < limInferiorIdade):
                                limInferiorIdade = idade
                            if(colesterol > limSuperiorColesterol):
                                limSuperiorColesterol = colesterol
                            if(colesterol < limInferiorColesterol):
                                limInferiorColesterol = colesterol
                        currEscalao = (idade//5)+1
                        if(currEscalao in doentesPorEscalaoEtario):
                            doentesPorEscalaoEtario[currEscalao] = (doentesPorEscalaoEtario[currEscalao]) + 1
                        else:
                            doentesPorEscalaoEtario[currEscalao] = 1
                        currNivelColesterol = (colesterol//10)+1
                        if(currNivelColesterol in doentesPorNivelColesterol):
                            doentesPorNivelColesterol[currNivelColesterol] = (doentesPorNivelColesterol[currNivelColesterol])+1
                        else:
                            doentesPorNivelColesterol[currNivelColesterol] = 1  
                        if(sexo == 'M'):
                            totalDoentesMasculinos = totalDoentesMasculinos + 1
                        if(sexo == 'F'):
                            totalDoentesFemininos = totalDoentesFemininos + 1
                buffer = f.readline()                     
        f.close()
    else:
        print("No such file.")


def distribuicaoPorSexo():
    global distribuicaoMasc 
    global distribuicaoFem

    distribuicaoMasc = (totalDoentesMasculinos / (totalDoentesMasculinos + totalDoentesFemininos)) * 100
    distribuicaoFem = (totalDoentesFemininos / (totalDoentesMasculinos + totalDoentesFemininos)) * 100

def distribuicaoEscalaoEtario(): 
    global distribuicaoPorEscEtario
    keys = range(len(doentesPorEscalaoEtario))
    values = list(doentesPorEscalaoEtario.values())
    for i in keys:
        distribuicaoPorEscEtario[i] = ((values[i])/(totalDoentesMasculinos + totalDoentesFemininos))*100

def distribuicaoNivelColesterol():
    global distribuicaoNivelCol
    keys = range(len(doentesPorNivelColesterol))
    values = list(doentesPorNivelColesterol.values())
    for i in keys:
        distribuicaoNivelCol[i] = ((values[i])/(totalDoentesMasculinos + totalDoentesFemininos))*100
    
def printTabelaPorSexo():
    print(f"| Sexo | % de doentes |")
    print("-----------------------")
    print(f"|  M   | "+ "%.2f"%distribuicaoMasc+ "        |")
    print(f"|  F   | "+ "%.2f"%distribuicaoFem+"         |")

def printTabelaEscEtario():
    print(f"| Escalao Etário | % de doentes |")
    print(f"---------------------------------")
    for i in distribuicaoPorEscEtario:
        limInferior = '{:0>2}'.format(((i-1)*5 + 5))
        limSuperior = '{:0>2}'.format(((i-1)*5 + 5)+4)
        espacos = '{:10}'.format(" ")
        print("["+limInferior+"-"+limSuperior+"]"+ espacos +"|", "%.2f"%distribuicaoPorEscEtario[i])

def printTabelaNivColesterol():
    print(f"| Nível Colesterol | % de doentes |")
    print(f"-----------------------------------")
    for i in distribuicaoNivelCol:
        limInferior = '{:0>3}'.format((i-1)*10 +10)
        limSuperior = '{:0>3}'.format(((i-1)*10 +10)+9)
        espacos = '{:10}'.format(" ")
        print(f"["+limInferior+"-"+limSuperior+"]"+espacos+"|", "%.2f"%distribuicaoNivelCol[i])

def main():
    readfile("myheart.csv")
    distribuicaoPorSexo()
    printTabelaPorSexo()
    print()
    distribuicaoEscalaoEtario()
    printTabelaEscEtario()
    print()
    distribuicaoNivelColesterol()
    printTabelaNivColesterol()

if __name__ == "__main__":
    main()
