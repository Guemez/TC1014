#yo soy 196
while (True):
    while(True):
        try:
            lower=int(input("Please give the lower bound: "))
            break
        except:
            print("That's not a valid input")

    while(True):
        try:
            upper=int(input("Please give the upper bound: "))
            break
        except:
            print("That's not a valid input")
    if upper<lower:
        print ("The lower bound must be lower than the upper bound")
    else:
        break

natural_palindromes=0
non_Lychrel=0
Lychrel_numbers=0

def invert(number):
    rebmun=int(str(number)[::-1])
    return rebmun

for x in range (lower, upper+1):
    y=invert(x)
    if x==y:
        natural_palindromes=natural_palindromes+1
    elif x!=y:
        n=x
        m=y
        counter=0
        while counter<=30:
            z=n+m
            if z==invert(z):
                non_Lychrel=non_Lychrel+1
                break
            elif counter<30:
                counter=counter+1
                n=z
                m=invert(z)
            elif counter==30:
                print ("Found a Lychrel: "+str(x))
                Lychrel_numbers=Lychrel_numbers+1
                break

print ("Natural palindromes: "+str(natural_palindromes))
print ("Non Lychrel numbers (become a palindrome): "+str(non_Lychrel))
print ("Lychrel numbers: "+str(Lychrel_numbers))
