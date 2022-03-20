import pandas as pd
import plotly.express as px
from datetime import date


potholes_1 = pd.read_csv("Python-Project-1/data/potholes_1.csv")
potholes_2 = pd.read_csv("Python-Project-1/data/potholes_1.csv")
potholes = pd.concat([potholes_1, potholes_2], ignore_index=True)

# This converts the creation and completion dates to datetime format so that you can measure time between the two.
potholes['CREATION DATE']= pd.to_datetime(potholes['CREATION DATE'])
potholes['COMPLETION DATE']= pd.to_datetime(potholes['COMPLETION DATE'])

# Shows the number days between completion date and creation date. With the average completion date per zipcode, you can make a map that hows which areas have the fastest or slowest average service time.
potholes['TIME_TO_COMPLETE'] = (potholes['COMPLETION DATE'] - potholes['CREATION DATE']).dt.days

#There are a lot of duplicate service request rows so this gets rid of them.
potholes = potholes.drop_duplicates(subset=['SERVICE REQUEST NUMBER'])


# For open potholes, you might want to check out which areas have had service requests opened for the longest time.
open_potholes = potholes.loc[potholes['STATUS'] == 'Open']
open_potholes['DAYS_OPEN'] = (pd.to_datetime('today').normalize() - potholes['CREATION DATE']).dt.days

# Interestingly, the average time that these service requests have been open are much longer than the average time it takes to complete a pothole.
