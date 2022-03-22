import pandas as pd

potholes = pd.read_csv(
    "data/311_Service_Requests_-_Pot_Holes_Reported_-_Historical.csv"
)

potholes_1 = potholes.iloc[0:250001]
potholes_2 = potholes.iloc[250001:]


potholes_1.to_csv("data/potholes_1.csv", index=False)
potholes_2.to_csv("data/potholes_2.csv", index=False)
