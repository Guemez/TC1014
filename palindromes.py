#palindromes

def filtrar(text):
    not_acceptable_but_with_space=[",",";",".","$","#","%","&","(",")","?",":","@","!"]
    filtered_words=text
    for i in not_acceptable_but_with_space:
        filtered_words=filtered_words.split(i)#eliminas los caracteres no aceptables
        filtered_words="".join(filtered_words)#juntas de nuevo el texto para que no quede separado como listas
    return filtered_words#regresa el texto filtrado


print("Hey, let's see if what you type is a palindrome")
user_input=str(input()).lower()
not_acceptable_characters=[",",";",".","$","#","%","&","(",")","?"," ",":","@","!"]#aqui tenemos espacio para checar si todo es un palindromo
filtered_input=user_input
for char in not_acceptable_characters:
    filtered_input=filtered_input.split(char)
    filtered_input="".join(filtered_input)

reversed_input=filtered_input[::-1]#voltea el string y lo compara con el normal
if reversed_input==filtered_input:
    print("The sentence  "+filtered_input+" is a palindrome")
else:
    print("The sentence  "+filtered_input+" is not a palindrome")

filtered=filtrar(user_input)#usamos la funcion

filtered_list=filtered.split()#la separamos en una lista con cada palabra

for word in filtered_list:
    if word==word[::-1]:#volteamos cada palabra y la comparamos con la normal
        print("The word "+word+" is a palindrome")
