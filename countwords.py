"""paragraph="input python egg python input input"
new=paragraph.split()
from collections import Counter
cnt=Counter(new)
print (cnt)"""

"""paragraph=str(input("I will count the times you repeat each word on your input: \n")).lower()
new=paragraph.split()
countedwords=[]
frecuency=[]
for word in range(0,len(new)):
    if new[word] not in (countedwords[:len(countedwords)]):
        countedwords.append(new[word])
        frecuency.append(1)
    else:
        number=countedwords.index(new[word])
        frecuency[number]=frecuency[number]+1
for items in range(0,len(countedwords)):
    print (str(countedwords[items])+": "+str(frecuency[items]))"""

def count_words(texto):
    contador={}
    listatexto=texto.split()
    for word in listatexto:
        if word not in contador:
            contador[word]=1
        else:
            contador[word]=contador[word]+1
    return contador

not_acceptable_but_with_space=[",",";",".","$","#","%","&","(",")","?",":","@","!"]
print ("Hola usuario, hoy contaremos la frcuencia de cada palabra en un texto introducido o abriendo un archivo .txt")
respuesta=str(input("Desea escribir el texto o abrir un archivo? [T/F] ")).lower()
if respuesta=="t":
    texto_usuario=str(input("Introduce el texto \n")).lower()
    filtered_words=texto_usuario
    for i in not_acceptable_but_with_space:
        filtered_words=filtered_words.split(i)
        filtered_words="".join(filtered_words)
    print(count_words(filtered_words))
else:
    text_file=input("Introduce el nombre del archivo que deseas abrir \n")
    archivo=open(text_file,'r')
    for line in archivo:
        archivo_nuevo=line.lower()
    filtered_words=archivo_nuevo
    for i in not_acceptable_but_with_space:
        filtered_words=filtered_words.split(i)
        filtered_words="".join(filtered_words)
    print(count_words(filtered_words))
