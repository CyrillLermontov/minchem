from src.data.functions import *
from src.data.sql_functions import *
import sqlite3

while True:
    try:
        count_of_elems = count_of_elements()

        users_input_data = input_data(count_of_elems)

        molar_masses_of_elements = get_molar_mass(users_input_data.keys())

        atom_quantities = atoms_quantities(users_input_data, molar_masses_of_elements)
        break
    except Exception:
        print("Попробуйте ещё раз!")
    finally:
        try:
            answer = input("Хотите попробовать ещё раз? д-да н-нет")

            if answer == "д":
                pass
            if answer == "н":
                print("Пока! Надеюсь ещё увидимся xD")
                raise SystemExit(1)
        except Exception:
            print("Я Вас не понимаю, ответьте на вопрос коректно!")
            pass

