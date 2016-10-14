#palindromes

def filtrar(text):
    not_acceptable_but_with_space=[",",";",".","$","#","%","&","(",")","?",":","@","!"]
    filtered_words=text
    for i in not_acceptable_but_with_space:
        filtered_words=filtered_words.split(i)
        filtered_words="".join(filtered_words)
    return filtered_words


print("Hey, let's see if what you type is a palindrome")
user_input=str(input()).lower()
not_acceptable_characters=[",",";",".","$","#","%","&","(",")","?"," ",":","@","!"]
filtered_input=user_input
for char in not_acceptable_characters:
    filtered_input=filtered_input.split(char)
    filtered_input="".join(filtered_input)

reversed_input=filtered_input[::-1]
if reversed_input==filtered_input:
    print("The sentence  "+filtered_input+" is a palindrome")
else:
    print("The sentence  "+filtered_input+" is not a palindrome")

filtered=filtrar(user_input)

filtered_list=filtered.split()

for word in filtered_list:
    if word==word[::-1]:
        print("The word "+word+" is a palindrome")
