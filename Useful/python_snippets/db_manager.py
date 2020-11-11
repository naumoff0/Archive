""" database management module """

import sqlite3


def query(db_name, table, search_category=None, value=None):
    """ querys a table in a database (both must be specified. if search category and requested value are left blank, \
        entire table will be returned in list tuple form """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # find values from the database
    if search_category and value:
        cursor.execute("SELECT * FROM {} WHERE {} = '{}';".format(table, search_category, sanitize(value)))
    else:
        cursor.execute("SELECT * FROM {}".format(table))

    rows = cursor.fetchall()

    connection.commit()
    connection.close()

    return rows


def add(db_name, table, columns, *values):
    """ adds row to table in a database """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    sanitized = sanitize(*values)

    cursor.execute("INSERT INTO {} ({}) VALUES {};".format(table, columns, sanitized))

    connection.commit()
    connection.close()


def execute(db_name, instruction):
    """ executes any given sql message. be sure to sanitize if user input is involved """

    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.executescript(instruction)

    connection.commit()
    connection.close()


def sanitize(*values):
    """ removes quotation marks from a list or tuple of values """
    def remove(value, values_to_remove):
        """ removes characters from a string """
        if isinstance(value, str):
            for char in values_to_remove:
                value = value.replace(char, "")

        return value

    if len(values) <= 1:
        value = values[0]
        return remove(value, ["\'", "\\\'", "\"", "\\\""])

    sanitized = []
    for value in values:
        if isinstance(value, (list, tuple)):
            value = sanitize(*value)

        elif isinstance(value, str):
            value = sanitize(value)

        sanitized.append(value)

    return tuple(sanitized)
