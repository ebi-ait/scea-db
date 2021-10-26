import argparse

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

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects('hca_project_uuid', 'hca_short_name', 'scea_status', 'scea_accession')
              VALUES (?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def main():

    parser = argparse.ArgumentParser(description="run hca -> scea tool")
    parser.add_argument(
        "-hca_project_uuid",
        type=str,
        required=True,
        help="Please provide the hca project uuid."
    )
    parser.add_argument(
        "-hca_short_name",
        type=str,
        required=True,
        help="Please provide the hca project short name."
    )
    parser.add_argument(
        "-scea_status",
        type=str,
        choices=['eligible', 'not eligible'],
        required=True,
        help="Please provide the scea status. Must be 1 of eligible or not eligible."
    )
    parser.add_argument(
        "--scea_accession",
        type=str,
        required=False,
        help="Please provide the assigned SCEA ID (E-HCAD) if the project is eligible."
    )
    args = parser.parse_args()

    database = r"hca2scea_db.sqlite"

    hca_project_uuid_input = args.hca_project_uuid
    hca_short_name_input = args.hca_short_name
    scea_status_input = args.scea_status
    scea_accession_input = args.scea_accession

    # create a database connection
    conn = create_connection(database)
    with conn:

        # create a new project
        project = (hca_project_uuid_input, hca_short_name_input, scea_status_input, scea_accession_input);
        project_id = create_project(conn, project)


if __name__ == '__main__':
    main()
