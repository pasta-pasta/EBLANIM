import math


#элементы
elems = ["fire", "earth", "water", "air", "lightning"]


runes_base = {"fehu": [elems[0], elems[1]],
              "uruz": [0],
              "turisaz": [elems[3], elems[4]],
              "ansuz": [elems[3], elems[2]],
              "raido": [elems[1], elems[3]],
              "kenaz": [elems[2], elems[0]],
              "gebo": [elems[2], elems[4]],
              "vunyo": [elems[1], elems[2]],
              "hagalaz": [elems[0], elems[3]],
              "nautiz": [0],
              "yera": [elems[4], elems[0]],
              "laguz": [elems[4], elems[1]],
              "isa": [elems[4], elems[3], elems[2]],
              "eyvaz": [0],
              "pert": [elems[2], elems[4], elems[1]],
              "algiz": [0],
              "soulu": [elems[1], elems[4], elems[0]],
              "teyvaz": [elems[0], elems[2], elems[4]],
              "berkanta": [elems[2], elems[1], elems[3]],
              "evaz": [elems[4], elems[0], elems[3]],
              "mannaz": [elems[3], elems[2], elems[0]],
              "inguz": [elems[3], elems[0], elems[1]],
              "odal": [elems[1], elems[3], elems[4]],
              "dagaz": [elems[0], elems[1], elems[2]]
              }

while True:
    try:
        current_elem = elems[int(input("Choose equation' element. 0 - fire, 1 - earth, 2 - water, 3 - air, 4 - lightning: "))]
        break
    except Exception as e:
        print(f"Exception {e}! Try again!")

equation = []

def is_finished(equation):
    pairs = 0
    elem = len(equation[-1])
    if len(equation) < 3:
        return False
    for i in range(len(equation)-1):
        elem += len(equation[i])
        for j in range(1, len(equation[i])):
            if equation[i][j] != equation[i][-1]:
                continue
            if equation[i][j] == equation[i+1][0]:
                pairs += 1
    if pairs == ((elem-2)/2) and equation[0][0] == equation[-1][-1]:
        return True
    if equation[0][0] == equation[-1][-1]:
        return "Closed!"
    return False

def calculate_force(equation):
    force = 0
    for i in equation:
        force += math.factorial(elems.index(i[0])+1)*math.factorial(elems.index(i[1])+1)
    return force/len(equation)

#Задали элемент. Пробежимся по списку рун, выберем подходящие, предложим юзеру выбрать
possible_first_runes = []
for rune, elem in runes_base.items():
    if elem[0] == current_elem:
        possible_first_runes.append(rune)
        eq_string = ""
        for j in runes_base[rune]:
            eq_string += f"-{j}"
        eq_string = eq_string[1:]
        print(f"Found first possible rune: {rune}! Equation will look as such: {eq_string}, ")
selected_rune = input("Write selected rune name: ")
equation.append(runes_base[possible_first_runes[possible_first_runes.index(selected_rune)]])

while True:
    possible_runes = []
    eq_string = ""
    eq_string_runes = ""
    if is_finished(equation) or is_finished(equation) == "Closed!":
        print(eq_string, end="")
        for i in equation:
            key = next(key for key, value in runes_base.items() if value == i)
            eq_string_runes += f"{key.upper()}, "
        print(eq_string_runes[:-2])
        print(f"Force: {calculate_force(equation)}")
        break
    for rune, elem in runes_base.items():
        if elem[0] == equation[-1][1]:
            possible_runes.append(rune)
            test_equation = equation.copy()
            test_equation.append(runes_base[possible_runes[possible_runes.index(rune)]])
            eq_string = ""
            for i in test_equation:
                for j in i:
                    eq_string += f"-{str(j)}"
                eq_string += ", "
            eq_string = eq_string[1:]
            if is_finished(test_equation) == True:
                print(
                    f"Found possible FINISHING rune: {rune}! Equation will look as such: {eq_string}, \n Force: {calculate_force(test_equation)}")
            elif is_finished(test_equation) == "Closed!":
                print(
                    f"Found possible CLOSING rune: {rune}! Equation will look as such: {eq_string}, \n Force: {calculate_force(test_equation)}")

            else:
                print(
                    f"Found possible rune: {rune}! Equation will look as such: {eq_string}, \n Force: {calculate_force(test_equation)}")

    selected_rune = input("Write selected rune name: ")
    equation.append(runes_base[possible_runes[possible_runes.index(selected_rune)]])
    eq_string = ""
    for i in equation:
        for j in i:
            eq_string += f"-{str(j)}"
        eq_string += ", "
    eq_string = eq_string[1:]
    print(eq_string)

if is_finished(equation) == "Closed!":
    unpaired_elements = []
    for i in range(len(equation)):
        for j in range(1, len(equation[i])):
            if equation[i][j] != equation[i][-1]:
                unpaired_elements.append([equation[i][j], equation[i]])
                continue

    print("\nUnpaired elements: ")
    for i in unpaired_elements:
        key = next(key for key, value in runes_base.items() if value == i[1])
        print(f"{i[0].upper()} at {i[1].index(i[0])+1} in rune {key.upper()} at {equation.index(i[1])+1}")