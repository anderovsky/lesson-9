subor = input("Zadaj meno suboru: ")
text = input("Zadaj text: ")
fileHandler = open(subor, "w")
fileHandler.write(text)
print(fileHandler)

fileHandler.close()