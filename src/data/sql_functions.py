import sqlite3


def get_molar_mass(elements):
    geologic_data = sqlite3.connect(r"C:\Users\Acer\Desktop\minchem\minchem\data\processed\geologic_data.db")
    cursor = geologic_data.cursor()

    cursor.execute("SELECT element_name, molar_mass FROM atoms_weight")
    items = cursor.fetchall()

    molar_masses = {}
    for el in items:
        if el[0] in elements:
            molar_masses[el[0]] = el[1]

    geologic_data.commit()

    return molar_masses


