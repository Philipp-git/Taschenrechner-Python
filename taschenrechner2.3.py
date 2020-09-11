def index_of(val, in_list):
    try:
        return in_list.index(val)
    except ValueError:
        return -1 

def to_list(userinput):
    userinput = userinput.replace(" ","")
    userinput = userinput.replace ("/",":")
    userinput = userinput.replace(",",".")
    userinput = userinput.replace ("÷",":")

    userinput = userinput.replace("+","split+split")
    userinput = userinput.replace("-","split-split")
    userinput = userinput.replace("*","split*split")
    userinput = userinput.replace(":","split:split")
    userinput = userinput.split("split")
    return userinput

def mal (userinput ):

    pos=userinput.index("*")
    erg = float(userinput[pos -1]) * float(userinput[pos +1])
    userinput = seterg(userinput,erg,pos)
    return (userinput )
    
def divi(userinput ):

  pos=userinput.index(":")
  try :
      erg = float(userinput[pos -1]) / float(userinput[pos +1])
  except ZeroDivisionError:
      print("ZeroDivisionError "+userinput [pos-1]+":" + userinput [pos +1])
      erg = float (userinput [pos -1])
      print("wird uebersprungen")
  userinput = seterg(userinput,erg,pos)
  return userinput 
def calculate(userinput):
    
    while True :
           
        malpos= index_of("*",userinput)
        divpos= index_of(":",userinput)
        if malpos > 0 and divpos > 0:
            if malpos<divpos:
                userinput = mal (userinput)
                continue 
            if divpos< malpos:
                pos = erg = 0
                pos=userinput.index(":")
                try :
                    erg = float(userinput[pos -1]) / float(userinput[pos +1])
                except ZeroDivisionError:
                    print("ZeroDivisionError "+userinput [pos-1]+":" + userinput [pos +1])
                    erg = float (userinput [pos -1])
                    print("wird uebersprungen")
                userinput = seterg(userinput,erg,pos)
                continue 
        else:
            if divpos > 0:
                userinput = divi(userinput )
                continue 
            if malpos>0:
                userinput = mal( userinput )
                continue 
            break 


    while True:
        if not index_of("+",userinput) == -1:
            pos = erg = 0
            pos=userinput.index("+")
            erg = float(userinput[pos -1]) + float(userinput[pos +1])
            userinput = seterg(userinput,erg,pos)
        else:
            break
            
    while True:
        if not index_of("-",userinput) == -1:
            pos = erg = 0
            pos=userinput.index("-")
            erg = float(userinput[pos -1]) - float(userinput[pos +1])
            #print (erg) debug
            userinput = seterg(userinput,erg,pos)
        else:
            break
    return userinput
    
def seterg(userinput,erg,pos):
    del userinput[pos-1]
    del userinput[pos-1]
    userinput[pos-1] = erg
    return(userinput)

print("taschenrechner2.3\nby philipp")
while True:
    
    userinput = str(input (">"))
    #userinput = "10:5*2" #debug 
    #print ( userinput ) debug 
    userinput = to_list (userinput)
    erg = calculate(userinput)[0]
    try:
        if erg == int(erg):
            print (int (erg))
    except all:
        print(erg)
  