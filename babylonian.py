#Babylonian method for square root
numb=float(input("Type a number and recieve the square root: "))

def Babylonian_square_root(number):
    guess=number/2
    error=0.000001
    guess2=(guess+number/guess)/2
    while abs(guess2-guess)>error:
        guess=guess2
        guess2=(guess+number/guess)/2
        #print (guess)
    return guess
answer=Babylonian_square_root(numb)
print("The Babylonian guess is: "+str(answer))
