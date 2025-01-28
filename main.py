subor = input("Zadaj meno suboru: ")
text = input("Zadaj text: ")
fileHandler = open(subor, "w")
fileHandler.write(text)
print(fileHandler)

print("Hello World")

fileHandler.close()