import os
import sqlite3
from functools import reduce
from sqlite3 import Error

import pandas as pd

from crimeretriever.constants import TABLE_NAME, CRIME_TYPE_NAME_MAP


def get_single_crime_type_for_period(db_conn, crime_type, start_date, end_date):
    db_crime_type = CRIME_TYPE_NAME_MAP[crime_type]
    query = """
            SELECT * FROM {tn}
            WHERE {tn}.CRIME_TYPE='{ct}' AND LATITUDE IS NOT NULL     
        """.format(tn=TABLE_NAME, ct=db_crime_type)
    crime_all_period = pd.read_sql(query, db_conn, parse_dates=["MONTH"], index_col="ID")

    crimes_selected_period = crime_all_period[
        (crime_all_period['MONTH'] >= start_date) & (crime_all_period['MONTH'] <= end_date)]
    return crimes_selected_period


def get_specific_crimes(db_conn, crime_types, start_date, end_date, output_csv_file_name):
    all_crime_types_list = map(lambda crime_type: get_single_crime_type_for_period(db_conn, crime_type, start_date, end_date), crime_types)
    all_crime_types = reduce(lambda df1, df2: df1.append(df2, ignore_index=True), all_crime_types_list)
    all_crime_types.to_csv(output_csv_file_name)


