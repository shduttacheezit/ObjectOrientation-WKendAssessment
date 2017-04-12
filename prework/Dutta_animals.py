animals = ["dog", "kitten", "koala bear", "sloth", "goat", "kangaroo"]
k_list = []

def find(letter): 
    i = 0
    while i < len(animals):
        for i in animals:
            if i[0] == letter:
                k_list.append(i)
    return k_list         

find("k")

print k_list