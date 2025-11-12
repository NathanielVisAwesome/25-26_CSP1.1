animals_list = ["dog", "cat", "mouse", "bird", "monkey"]
print(animals_list)

animals_list.append("otter")
print(animals_list)

for animal in animals_list:
    print(animal)

empty = " "

for i in empty*2:
    print(i)

animals_list.remove("mouse")
for animal in animals_list:
    print(animal)
