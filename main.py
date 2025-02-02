subor = input("Zadaj meno suboru ktory chces vytvorit: ")
text = input("Zadaj text ktorý sa zapíše do súboru: ")
fileHandler = open(subor, "w")
fileHandler.write(text)
print(fileHandler)

print("Hello World")

fileHandler.close()