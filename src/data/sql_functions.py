import sqlite3


def get_molar_mass(elements):
    """
    This function searches for paint mass based on the data entered by the user.
    The table "atoms_weight" from the database "geologic_data" is used for this purpose.
    By iterating with a loop, the function enumerates the paint weights from the table and
    writes the necessary ones to the dictionary.
    """
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


def get_mineral(users_input_data):
    """
    This function gets the name of the mineral based on the data entered by the user.
    Using the table "minerals_cations", the function finds the mineral in which the elements correspond
    to those entered by the user, and the mass % correspond with an error of 10%.
    """
    geologic_data = sqlite3.connect(r"C:\Users\Acer\Desktop\minchem\minchem\data\processed\geologic_data.db")
    cursor = geologic_data.cursor()

    cursor.execute("SELECT * FROM minerals_cations")
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in cursor.fetchall()]

    new_data = []
    for mineral in data:
        counter = {}
        for el in users_input_data:
            if (mineral[el] is not None and
                    users_input_data[el] - users_input_data[el] * 0.1 < float(mineral[el].replace(",", ".")) <
                    users_input_data[el] + users_input_data[el] * 0.1):
                counter[el] = mineral[el]
        if len(counter) == len(users_input_data):
            new_data.append(mineral["ID_mineral"])

    geologic_data.commit()

    return new_data

