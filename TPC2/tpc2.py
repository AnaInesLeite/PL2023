#TPC 2 - A96159
import io
import sys

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def readinput():
    soma = 0.0
    initState = "Off"
    text = input()
    while (text.upper() != "ON"):
        text = input()
    if(text.upper() == "ON"):
        initState = "On"
        text = input()
        while(text != "="):
#            print(initState)
            while(initState == "On"):
                if(text.isnumeric() == True or is_float(text) == True ):
                    soma += float(text)
                if(text == "=" and initState == "On"):
                    print(str(soma))
                    break
                if(text.upper() == "OFF"):
                    initState = "Off"
                text = input()
            text = input()
            if text.upper() == "ON":
                initState = "On"

            
def main():
    readinput()

if __name__ == "__main__":
    main()