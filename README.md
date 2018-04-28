# About
This repository is a little manual on how to access London [Police Data](https://data.police.uk/) in a more user-friendly way than downloading separate CSV files. Note that this offers data only for London even though the portal offers data for the whole country.

# The dataset
The dataset contains the following information for each crime that happened in London:
1. Month and year
2. Latitude, Longitude
3. Short description
4. Crime type

## Crime types mapping

The mapping below is important when passing arguments to the scripts in this package. The CSV downloaded from the [police](data.police.uk)
website uses the names as in the second column of the below table. When using these scripts, whenever a crime type is required
please use the first column of the table.


| Internal name               |         Official data.police.uk name
| ---------------------------------------------------------------------
| theft-from-person           |         Theft from the person
| vehicle-crime               |         Vehicle crime
| shoplifting                 |         Shoplifting
| violence-sexual-offences    |         Violence and sexual offences
| anti-social-behaviour       |         Anti-social behaviour
| burglary                    |         Burglary
| robbery                     |         Robbery
| criminal-damage-arson       |         Criminal damage and arson
| other-theft                 |         Other theft
| possession-weapons          |         Possession of weapons
| other-crime                 |         Other crime
| public-order                |         Public order
| drugs                       |         Drugs
| bicycle-theft               |         Bicycle theft
| violent-crime               |         Violent crime
| public-disorder-weapons     |         Public disorder and weapons
        

# Steps to retrieve the data
1. Download the dataset from [Kaggle](kaggle.com/jp2011/london-crime) as `crime.db` file.
2. Either use SQLite directly by loading `crime.db` that you downloaded in step 1, or use the provided python scripts to generate CSV files for a specific time interval and for specific crime types.

# Examples of usage

## Generate a CSV file for specific crime types for a specific range
```python
python3 -m crimeretriever.command getcsv --dbfile ./crime.db --startdate 2015-01-01 --enddate 2015-01-31 --crimetypes burglary theft-from-person --outfile 'export.csv'
```

The columns in the generate CSV are: 
```sql
INDEX, MONTH, LATITUDE, LONGITUDE, DESCRIPTION, CRIME_TYPE
```


# Warnings
Please, regularly check [the Changelog](https://data.police.uk/changelog/) for any issues with the data.

Currently, for London data, the following issues are not yet resolved:
1. City of London data for the period starting on Sep 2017 until present are not yet available due to change of IT infrastructure at the CoL police.

# Advanced Usage
## Regenerate the database from CSV files
```python
python3 -m crimeretriever.command builddb --dbfile --rootpath ./path-to-folder-with-uk-police-csvs
```

# Licence
The data are originally licensed by [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). This manual, and the accompanying source code is licensed under MIT License - see [LICENCE.md](./LICENCE.md)
