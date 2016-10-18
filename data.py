
def analisis(lowbound,highbound):
    text=open("cars.txt", 'r')
    new=[]
    new_new=[]
    for line in text:
        new.append(line[lowbound:highbound])
    for x in range(0,len(new)-1):
        if (x%2)==0:
            new_new.append(float(new[x]))
    return new_new

def average(lista):
    average=0
    for number in lista:
        average=average+number
    average=average/len(lista)
    return average

MPG=analisis(52,54)
HMPG=analisis(55,57)
mid_price=analisis(42,46)

average_MPG=average(MPG)
average_HMPG=average(HMPG)
average_mid=average(mid_price)

print ("The average miles per galon is "+str(average_MPG))
print ("The average miles per galon in highway is "+str(average_HMPG))
print ("The average midrange price is $"+str((average_mid)*1000))
