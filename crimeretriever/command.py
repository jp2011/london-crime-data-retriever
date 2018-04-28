import sqlite3
from argparse import ArgumentParser
from datetime import datetime

from crimeretriever.databasebuilder import db_bootstrap
from crimeretriever.retrieve import get_specific_crimes


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except sqlite3.Error as e:
        print(e)
        conn.close()


def process():
    print("Processing commands")
    parser = ArgumentParser(description="London Crime Retriever Parser")
    parser.add_argument('action')
    parser.add_argument('--dbfile', '-d', type=str, required=True, help='Please give a path to the crime.db file.')
    parser.add_argument('--rootpath', '-rp', type=str)
    parser.add_argument('--startdate', '-sd', type=str)
    parser.add_argument('--enddate', '-ed', type=str)
    parser.add_argument('--outfile', '-o', type=str)
    parser.add_argument('-c', '--crimetypes', nargs='+', help='Add crime types separated by a comma')

    arguments = parser.parse_args()

    action = arguments.action
    db_file = arguments.dbfile

    db_connection = create_connection(db_file)

    if action == "builddb":
        root_path = arguments.rootpath
        db_bootstrap(db_connection, root_path)

    if action == "getcsv":
        start_date = datetime.strptime(arguments.startdate, '%Y-%m-%d')
        end_date = datetime.strptime(arguments.enddate, '%Y-%m-%d')
        crime_types = arguments.crimetypes
        out_csv_file_name = arguments.outfile

        get_specific_crimes(db_connection, crime_types, start_date, end_date, out_csv_file_name)

if __name__ == "__main__":
    process()
