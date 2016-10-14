#Bubble sort

def is_sorted(lista):
    for i in range(len(lista)-1):
        if(lista[i] > lista[i+1]):
            return False
    return True

def bubble(listas):
    global contador
    test=is_sorted(listas)
    while test==False:
        contador=contador+1
        for index in range(0,len(listas)-1):
            if listas[index]>listas[index+1]:
                (listas[index],listas[index+1])=(listas[index+1],listas[index])
        test=is_sorted(listas)
    return listas

print("Let's check if the numbers are in order")
numbers=int(input("How many numbers would you like to try? "))
print ("OK, now give me the numbers")
list_of_numbers=[]
for i in range(1,numbers+1):
    user_number=int(input("Number "+str(i)+": "))
    list_of_numbers.append(user_number)
contador=1

print(bubble(list_of_numbers))
print (contador)
