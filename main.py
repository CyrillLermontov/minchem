from src.data.functions import *
from src.data.sql_functions import *
import sqlite3

while True:
    try:
        count_of_elems = count_of_elements()

        users_input_data = input_data(count_of_elems)

        molar_masses_of_elements = get_molar_mass(users_input_data.keys())

        atom_quantities = atoms_quantities(users_input_data, molar_masses_of_elements)

        name_of_mineral = get_mineral(users_input_data)
        print(name_of_mineral)
        break
    except Exception:
        print("Данные введены некоректно!")
        answer = input("Хотите попробовать ещё раз? д-да н-нет")

        if answer == "д":
            pass
        if answer == "н":
            print("Пока! Надеюсь ещё увидимся xD")
            raise SystemExit(1)


