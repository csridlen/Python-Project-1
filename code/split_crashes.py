import pandas as pd
crashes = pd.read_csv('traffic_crashes.csv', usecols=('CRASH_RECORD_ID','CRASH_DATE','ROAD_DEFECT', 'LATITUDE', 'LONGITUDE', 'LOCATION'))


crash_1 = crashes.iloc[0:300000].loc[crashes['ROAD_DEFECT'] == 'RUT, HOLES']
crash_2 = crashes.iloc[300000:].loc[crashes['ROAD_DEFECT'] == 'RUT, HOLES']

crash_1.to_csv('crashes_1.csv',index=False)
crash_2.to_csv('crashes_2.csv',index=False)
