abecedario=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r","s","t","u", "v", "w", "x", "y", "z"]

def letters(text):
    letras={}#we create a dictionary to store the letter with is't respective value
    new_text=text.lower()#we make the user input lowercase
    for letter in abecedario:
        times=new_text.count(letter)#the function counts whatever char you specify
        if times==0:#if a letter is not in the text we do not put it in the dictionary
            continue#we return to the for
        else:
            letras[letter]=times#we append to the dictionary the letter with the value of times that it repeated
    return letras

print ("We will count how many times you repeat each letter in a text")
user=str(input("Type a string: "))#we ask the user for a string to count the letters of
answer=letters(user)#we run the function
print (answer)
