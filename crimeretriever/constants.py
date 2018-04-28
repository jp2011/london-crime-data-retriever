

TABLE_NAME = "LONDON"
CSV_COL_NAMES = ["Month", "Latitude", "Longitude", "Location", "Crime type"]
DB_COL_NAMES = ["MONTH", "LATITUDE", "LONGITUDE", "DESCRIPTION", "CRIME_TYPE"]
DB_COL_TYPES = ["TEXT", "REAL", "REAL", "TEXT", "TEXT"]



CRIME_TYPE_NAME_MAP = {
        "theft-from-person": "Theft from the person",
        "vehicle-crime": "Vehicle crime",
        "shoplifting": "Shoplifting",
        "violence-sexual-offences": "Violence and sexual offences",
        "anti-social-behaviour": "Anti-social behaviour",
        "burglary": "Burglary",
        "robbery": "Robbery",
        "criminal-damage-arson": "Criminal damage and arson",
        "other-theft": "Other theft",
        "possession-weapons": "Possession of weapons",
        "other-crime": "Other crime",
        "public-order": "Public order",
        "drugs": "Drugs",
        "bicycle-theft": "Bicycle theft",
        "violent-crime": "Violent crime",
        "public-disorder-weapons": "Public disorder and weapons",
    }