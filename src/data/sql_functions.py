import sqlite3


def get_molar_mass(elements):
    try:
        geologic_data = sqlite3.connect(r"C:\Users\Acer\Desktop\minchem\minchem\data\processed\geologic_data.db")
        cursor = geologic_data.cursor()

        cursor.execute("SELECT element_name, molar_mass FROM atoms_weight")
        items = cursor.fetchall()

        molar_masses = {}
        for el in items:
            if el[0] in elements:
                molar_masses[el[0]] = el[1]
            if el[0] not in elements:
                raise ValueError('A very specific bad thing happened.')

        geologic_data.commit()

        return molar_masses
    except Exception:
        print("Данные химических элементов введены некоректно.\nПроверьте вводимые Вами данные и попробуйте снова.")



