user=str(input("Type a string: "))
new_user=user.lower()
times=new_user.count("a")
letter=str(input("What letter do you want me to count? ")).lower()

def letters(letter):
    times=new_user.count(letter)
    return times


answer=letters(letter)

print ("The letter "+str(letter)+" is "+str(times)+" times in the sentence "+str(new_user))
