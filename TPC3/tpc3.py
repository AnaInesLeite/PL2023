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

    countLines = 0
   
    if(f != None):
        dict20Lines = {}
        buffer = f.readline()
        while (buffer != ""):
            countLines += 1
            if(countLines<20):
                dict20Lines[countLines-1] = buffer
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
                    for i in parente:
                        if i in dictPorRelacao:
                            dictPorRelacao[i]+=1
                        else:
                            dictPorRelacao[i] = 1
            buffer = f.readline()
        outputFile = open("./file.json", "w")
        json.dump(dict20Lines, outputFile)
        outputFile.close()
        f.close()                             
    else:
        print("No such file")

def calcFrequencia():
    totalAnos = sum(dictPorAno.values())
    freqAnos = 0.0

    totalRelacoes = sum(dictPorRelacao.values())
    freqRelacao = 0.0
    
    espacos = '{:10}'.format(" ")
    espacosRelacoes = '{:30}'.format(" ")

    print("Ano"+espacos+"Frequência")
    for i in dictPorAno:
        freqAnos = (float)(dictPorAno[i]/totalAnos)*100    
        print(str(i)+espacos+"%.3f"%freqAnos)    

    print('{:>20}'.format("Relação")+espacosRelacoes+"Frequência")
    for i in dictPorRelacao:
        freqRelacao =  (float)(dictPorRelacao[i]/totalRelacoes)
        print('{:>20}'.format(str(i))+espacosRelacoes+"%.3f"%freqAnos)
    

def main():
    readfile("processos.txt")
    calcFrequencia()
    return 0

if __name__ == "__main__":
    main()    


    