import os

palRes=["and","or","xor","__FILE__","exception",
"__LINE__","array","as","break","case",
"class","const","continue","declare","default",
"die","do","echo","else","elseif",
"empty","enddeclare","endfor","endforeach","endif",
"endswitch","endwhile","eval","exit","extends",
"for","foreach","function","global","if",
"include","include_once","isset","list","new",
"print","require","require_once","return","static",
"switch","unset","use","var","while",
"__FUNCTION__","__CLASS__","__METHOD__","final","php_user_filter",
"interface","implements","extends","public","private","protected","abstract","clone",
"try","catch","throw","cfunction","old_function","this","namespace","import","goto"]		


def esSeparador(caracter):
    return caracter in " \n\t"

def esSimboloEsp(caracter):
    return caracter in "+-*;,.:!=%&/()[]<><=>=:=$"

def esEntero(cad):
    valido = True
    for c in cad:
        if c not in "0123456789":
            valido = False
    return valido

def esOperador(caracter):
    return caracter in "+-*/"

def tokeniza(linea):
    tokens = []
    dentro = False   
    for l in linea:
        if esSimboloEsp(l) and not(dentro):
            tokens.append(l)
        if (esSimboloEsp(l) or esSeparador(l)) and dentro:
            tokens.append(cad)
            dentro = False
            if esSimboloEsp(l):
                tokens.append(l)
        if not (esSimboloEsp(l)) and not (esSeparador(l)) and not(dentro):
            dentro = True
            cad=""
        if not (esSimboloEsp(l)) and not (esSeparador(l)) and dentro:
                cad = cad + l   
    return tokens

def quitadoblediag(archivoEnt):
    archivo=open(archivoEnt,"r")
    texto=[]
    cad=""
    for linea in archivo:
        texto.append(linea)
    archivo.close()
    archivo=open(archivoEnt,"w")
    indAux=0
    for linea in texto:
        if "//" in linea:
            indAux=linea.find("//")
            tokens=tokeniza(linea[indAux:])
            print(tokens)
            bander=False
            if((len(tokens)==2) or (tokens[2] in palRes) or (esSimboloEsp(tokens[2]))):
                bander=True 
            if(bander):
                linea=linea[0:indAux]+"\n"
            
        archivo.write(linea)
    archivo.close()
    return None

def comentCarpeta(ruta):
    if ruta=="":
        contenido=os.listdir()
    else:
        contenido=os.listdir(ruta)
    for i in contenido:
        if(os.path.isdir(os.path.join(ruta, i))):
            print(i+" Es directorio")
            comentCarpeta(ruta+"/"+i)
        if i.endswith(".php"):
            if ruta=="":
                quitadoblediag(i)
            else:
                quitadoblediag(ruta+"/"+i)
        
ruta=input("dame la ruta: ")
comentCarpeta(ruta)
#quitadoblediag("consumption.php")