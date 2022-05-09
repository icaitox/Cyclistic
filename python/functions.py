import pandas as pd 
from datetime import datetime

def tripnday(df):
#This function receives a dataFrame and adds some columns: 'trip_length' and 'week_day'.

    #Converting to datetime64 datatypes
    df['ended_at'] = pd.to_datetime(df['ended_at'])
    df['started_at'] = pd.to_datetime(df['started_at'])

    #Getting the trip length as the difference between at what time it ended and when it started
    df['trip_length'] = df['ended_at'] - df['started_at']

    #Getting the weekday with the date
    df['week_day'] = df['started_at'].dt.day_name()

    #Categorizing timeFrame
    df['time_frame'] = pd.cut(df['started_at'].dt.hour,
       bins=[0, 6, 12, 18, 24],
       labels=['night', 'morning', 'afternoon', 'evening'],
       right=False,
       include_lowest=True)

    #Returns sorted values
    return df.sort_values('started_at')


def clean(df):
   #This function receives a dataFrame and returns another dataframe which only contains trip_lengths greater than 90 seconds but less than 1 day.
   df['trip_length'] = pd.to_timedelta(df['trip_length'])
   newDf = df[df['trip_length'] < '1 days 00:00:00']
   newDf = newDf[newDf['trip_length'] > '0 days 00:01:30']

   return newDf
