import pandas as pd
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
