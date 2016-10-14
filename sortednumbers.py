import random

def is_sorted(lista):
    for i in range(len(lista)-1):
        if(lista[i] > lista[i+1]):
             return False
     return True

print("Let's check if the numbers are in order")
numbers=int(input("How many numbers would you like to try? "))
print ("OK, now give me the numbers")
list_of_numbers=[]
counter=1
for i in range(1,numbers+1):
    user_number=int(input("Number "+str(i)+": "))
    list_of_numbers.append(user_number)

test=is_sorted(list_of_numbers)

while test==False:
    new_number=numbers
    new_list_of_numbers=[]
    counter=counter+1
    for x in range(1, len(list_of_numbers)+1):
        index=random.randint(0,new_number-1)
        new_number=new_number-1
        new_list_of_numbers.append(list_of_numbers[index])
        del list_of_numbers[index]
    list_of_numbers=new_list_of_numbers
    print (list_of_numbers)
    test=is_sorted(list_of_numbers)

print ("The list "+str(list_of_numbers)+" is in order")
print ("It took "+str(counter)+" tries to get it in order")
