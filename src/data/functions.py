def count_of_elements():
    """
    Entering the number of elements
    """
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
    """
    Element entry function.
    Depending on the selected quantity, the data is written to the "chemical element: mass percentages" dictionary.
    """
    users_inputs = {}
    for i in range(count_of_elems):
        key = input('Введите химический элемент: ')
        value = input('Введите его содержание в мас.%: ')
        users_inputs[key] = float(value)
    return users_inputs


def atoms_quantities(users_input, molar_masses):
    """
    This function calculates atomic masses.
    Mass Percentage / Paint Mass.
    """
    atoms_quants = {}
    for key in users_input.keys():
        atoms_quants[key] = round(users_input[key] / molar_masses[key], 3)
    return atoms_quants

