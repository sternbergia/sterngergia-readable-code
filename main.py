path = "./dictionary-data.txt"

file = open(path, mode="r", encoding="UTF-8")

dictionary = {}
ID = 1
for word in file.readlines():
    dictionary[ID] = word.strip()
    ID += 1

for id in dictionary.keys():
    print(str(id) + ": " + dictionary[id])

file.close()
