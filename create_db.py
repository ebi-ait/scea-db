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

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():


    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects(
                                        id integer PRIMARY KEY,
                                        hca_project_uuid text NOT NULL,
                                        hca_short_name text NOT NULL,
                                        scea_status text NOT NULL,
                                        scea_accession text
                                    ); """

    # create a database connection
    conn = create_connection(r"hca2scea_db.sqlite")

    # create table
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()        
