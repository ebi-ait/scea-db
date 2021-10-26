import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def get_accessions_set(conn):

    sql = ''' SELECT scea_accession FROM projects '''
    cursor = conn.cursor()
    data = cursor.execute(sql)
    accessions_list = []
    for row in data:
        accessions_list.append(row[0])
    return set(accessions_list)


def get_next_accession(conn):

    unique_accessions = get_accessions_set(conn)
    print(unique_accessions)
    accessions_numbers = [int(accession.split("E-HCAD-")[1]) for accession in unique_accessions if "E-HCAD" in accession]
    next_accession = "E-HCAD-" + str(max(accessions_numbers) + 1)
    return next_accession


def main():

    database = r"hca2scea_db.sqlite"

    # create a database connection
    conn = create_connection(database)
    with conn:

        # Get the next accession
        accession = get_next_accession(conn)
        print(accession)


if __name__ == '__main__':
    main()
