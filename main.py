path = "./dictionary-data.txt"

file = open(path, mode="r", encoding="shift-JIS")

dictionary = []
for word in file.readlines():
    dictionary.append(word.strip())

print(*dictionary, sep="\n")

file.close()
