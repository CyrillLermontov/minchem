from src.data.functions import *
from src.data.sql_functions import *
import sqlite3


count_of_elements = int(input('Введите, какое количество элементов вы планируете задать: '))

users_input_data = input_data(count_of_elements)

molar_masses_of_elements = get_molar_mass(users_input_data.keys())
print(molar_masses_of_elements)