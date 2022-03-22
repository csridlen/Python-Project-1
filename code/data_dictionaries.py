import pandas as pd

### Potholes data
potholes_1 = pd.read_csv("data/potholes_1.csv")
# print(pd.unique(potholes["SSA"]) i used this to return unique values from a specific column

potholes_dict = {
    'Columns' : list(potholes_1.columns),
    'Description' : ['date service request was created',
                     'status of the request',
                     'date service request has been resolved',
                     'id of service request',
                     'type of service request (only potholes in this data set)',
                     'work being done currently (null if none)',
                     'latest activity done on request',
                     'number of potholes filled on block',
                     'street address',
                     'zipcode',
                     'x coordinate',
                     'y coordinate',
                     'ward (there are 50 in chicago)',
                     'police district',
                     'community area of chicago used for statistical and planning purposes',
                     'special service area (tax district)',
                     'latitude',
                     'longitude',
                     '(latitude, longitude)'],
}
potholes_data_dictionary = pd.DataFrame.from_dict(potholes_dict)
potholes_data_dictionary.to_csv("data/potholes_data_dictionary.csv", index=False)

# detailed descriptions for data can be found here: https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Pot-Holes-Reported-Historical/7as2-ds3y


### Traffic crash data
crashes_1 = pd.read_csv("data/crashes_1.csv")
crashes_dict = {
    'Columns' : list(crashes_1.columns),
    'Description' : ['id of crash, unique',
                     'date and time of crash',
                     'road defects, as determined by reporting officer',
                     'latitude',
                     'longitude',
                     '(latitude, longitude)'],
}

crash_data_dictionary = pd.DataFrame.from_dict(crashes_dict)
crash_data_dictionary.to_csv("data/crash_data_dictionary.csv", index=False)

# detailed descriptions of omitted columns can be found here: https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if


### Census data
census = pd.read_csv("data/chicago_census_data.csv")
census_dict = {
    'Columns' : list(census.columns),
    'Description' : ['community area of chicago used for statistical and planning purposes',
                     'name of community area',
                     'percent occupied housing units with more than one person per room',
                     'percent of households living below federal poverty line',
                     'percent aged 16+ unemployed',
                     'percent aged 25+ who didnt graduate high school',
                     'percent aged under 18 or over 64 (dependants)',
                     'income per capita',
                     'Score that incorporates each of the six selected socioeconomic indicators'],
}
census_data_dictionary = pd.DataFrame.from_dict(census_dict)
census_data_dictionary.to_csv("data/census_data_dictionary.csv", index=False)

# detailed descriptions for data can be found here: https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2


### Arrest data
arrest = pd.read_csv("data/PublicReleaseArrestDataUPDATE.csv")
arrest_dict = {
    'Columns' : list(arrest.columns),
    'Description' : ['chicago police district where arrest took place',
                     'chicago police beat (patorl territory) where arrest took place',
                     'arrest year',
                     'arrest month',
                     'perceived race code of arrested',
                     'crime type code reported to fbi',
                     'statute that arrested person was charged with violating',
                     'statute description',
                     'class of the charge',
                     'level of charge (misdemeanor or felony)'],
}
arrest_data_dictionary = pd.DataFrame.from_dict(arrest_dict)
arrest_data_dictionary.to_csv("data/arrest_data_dictionary.csv", index=False)

# detailed descriptions for data can be found here: https://home.chicagopolice.org/statistics-data/public-arrest-data/
