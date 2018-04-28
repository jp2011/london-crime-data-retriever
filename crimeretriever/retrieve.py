import os
import sqlite3
from sqlite3 import Error

import pandas as pd

from crimeretriever.constants import TABLE_NAME


def get_specific_crimes(db_conn, crime_types, start_date, end_date, output_csv_file_name):
    query = """
        SELECT * FROM {tn}
        WHERE {tn}.CRIME_TYPE='{ct}' AND LATITUDE IS NOT NULL     
    """.format(tn=TABLE_NAME, ct=crime_type)
    crime_all_period = pd.read_sql(query, db_conn, parse_dates=["MONTH"], index_col="ID")

    crimes_selected_period = crime_all_period[(crime_all_period['MONTH'] >= start_date) & (crime_all_period['MONTH'] <= end_date)]
    crimes_selected_period.to_csv(output_csv_file_name)


