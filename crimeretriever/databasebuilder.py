import os
import sqlite3
import pandas as pd

from crimeretriever.constants import TABLE_NAME, DB_COL_TYPES, DB_COL_NAMES, CSV_COL_NAMES


def list_files(startpath):
    full_file_paths = []
    for root, directories, filenames in os.walk(startpath):
        for filename in filenames:
            if filename.endswith('.csv'):
                full_file_paths.append(os.path.join(root, filename))
    return full_file_paths


def create_crime_table(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("CREATE TABLE {tn} (ID INTEGER)".format(tn=TABLE_NAME))

    for (col_name, col_type) in zip(DB_COL_NAMES, DB_COL_TYPES):
        cursor.execute("ALTER TABLE {tn} ADD COLUMN {cn} {ct}".format(tn=TABLE_NAME, cn=col_name, ct=col_type))


def move_csv_to_sql(sql_conn, csv_file_paths):
    for file_path in csv_file_paths:
        print("Processing: " + file_path)
        crime_df = pd.read_csv(file_path, usecols=CSV_COL_NAMES)
        crime_df.columns = DB_COL_NAMES
        crime_df.to_sql(TABLE_NAME, sql_conn, if_exists='append', index_label="ID")


def db_bootstrap(db_conn, root_path):
    try:
        create_crime_table(db_conn)
    except sqlite3.OperationalError as error:
        print(error)
    all_crime_csv_file_paths = list_files(root_path)
    move_csv_to_sql(db_conn, all_crime_csv_file_paths)


