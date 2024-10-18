string = input("Insira uma string: ")

count = string.count("a") + string.count("A")

if count > 0:
    print(f"A letra 'A' apareceu {count} vezes")
else:
    print("A letra 'A' não apareceu")
