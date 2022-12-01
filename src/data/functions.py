def count_of_elements():
    while True:
        try:
            count_of_elems = int(input("Введите, какое количество элементов вы планируете задать: "))
            break
        except Exception:
            print("Попробуйте ввести количество элементов ещё раз!\nВводимые данные не должны включать "
                  "символы, буквы любого алфавита.")
            pass
    return count_of_elems


def input_data(count_of_elems):
    users_inputs = {}
    for i in range(count_of_elems):
        key = input('Введите химический элемент: ')
        value = input('Введите его содержание в мас.%: ')
        users_inputs[key] = float(value)
    return users_inputs


def atoms_quantities(users_input, molar_masses):
    atoms_quants = {}
    for key in users_input.keys():
        atoms_quants[key] = users_input[key] / molar_masses[key]
    return atoms_quants

