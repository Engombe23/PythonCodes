# Assessed Task 3 Week 5

text = input("Enter text to analyse: ")

count = 0

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

textInChars = []

for i in range(len(text)):
    textInChars.append(text[i])
       
for j in range(len(alphabet)):
    for k in range(len(textInChars)):
        if alphabet[j] == textInChars[k]:
            count += 1
        
    print("Letter " + alphabet[j] + " - Frequency =", count)
    count = 0