def input_data(count_of_elements):
    users_inputs = {}
    for i in range(count_of_elements):
        key = input('Введите химический элемент: ')
        value = input('Введите его содержание в мас.%: ')
        users_inputs[key] = float(value)
    return users_inputs
