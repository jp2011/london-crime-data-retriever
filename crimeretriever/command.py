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
    parser.add_argument('--rootpath', '-rp', type=str, help="File path to a folder which contains CSV with raw data.")
    parser.add_argument('--startdate', '-sd', type=str, help="Date range for retrieval: start date (inclusive)")
    parser.add_argument('--enddate', '-ed', type=str, help="Date range for retrieval: end date (inclusive)")
    parser.add_argument('--outfile', '-o', type=str, help="Path to the new CSV file that will be generated.")
    parser.add_argument('--crimetypes', '-c', nargs='+', help='Add crime types separated by a comma')

    arguments = parser.parse_args()

    action = arguments.action
    db_file = arguments.dbfile

    db_connection = create_connection(db_file)

    if action == "builddb":
        # read action specific args
        root_path = arguments.rootpath

        # execute the action
        db_bootstrap(db_connection, root_path)

    if action == "getcsv":
        # read action specific args
        start_date = datetime.strptime(arguments.startdate, '%Y-%m-%d')
        end_date = datetime.strptime(arguments.enddate, '%Y-%m-%d')
        crime_types = arguments.crimetypes
        out_csv_file_name = arguments.outfile

        # execute the action
        get_specific_crimes(db_connection, crime_types, start_date, end_date, out_csv_file_name)

    db_connection.close()

if __name__ == "__main__":
    process()
