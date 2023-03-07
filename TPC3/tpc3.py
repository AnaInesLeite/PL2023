#TPC3 - A96159
import json
import re

dictPorAno = {}
dictPorRelacao = {}

#função que lẽ o ficheiro
def readfile(fullFileName):

    global dictPorAno
    global dictPorRelacao

    f = open(fullFileName, "r")
   
    if(f != None):
        buffer = f.readline()
        while (buffer != ""):
            size = len(buffer)-1
            itens = (buffer[:size]).split("::")
            if(itens != None):
                if(len(itens) ==7):
                    data = itens[1]
                    ano = data.split("-")[0]
                    if ano in dictPorAno:
                        dictPorAno[ano] +=1
                    else:
                        dictPorAno[ano] = 1
                    parentes = itens[5]
                    parente = re.findall(r'\,([A-Za-z]+[\s]*[A-Za-z]*\.)', parentes)
                    r = len(re.findall(r'\,([A-Za-z]+[\s]*[A-Za-z]*\.)', parentes))
                    print(parente)
                    for i in parente:
                        if i in dictPorRelacao:
                            dictPorRelacao[i]+=1
                        else:
                            dictPorRelacao[i] = 1
            buffer = f.readline()
        f.close()                             
    else:
        print("No such file")

def calcFrequencia():
    totalAnos = sum(dictPorAno.values())
    freqAnos = 0.0

    totalRelacoes = sum(dictPorRelacao.values())
    freqRelacao = 0.0
    
    for i in dictPorAno:
        freqAnos = (float)(dictPorAno[i]/totalAnos)*100     
    for i in dictPorRelacao:
        freqRelacao =  (float)(dictPorRelacao[i]/totalRelacoes)

def main():
    readfile("processos.txt")
    return 0

if __name__ == "__main__":
    main()    