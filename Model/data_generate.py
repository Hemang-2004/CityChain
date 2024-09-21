import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def create():

    # Parameters
    num_bins = 100
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 7, 1)
    bins = range(1, num_bins + 1)

    # Create timestamp list
    timestamps = pd.date_range(start=start_date, end=end_date, freq='h').to_pydatetime().tolist()

    # Data storage
    data = []

    # Simulate data
    for bin_id in bins:
        last_collection_time = start_date
        for current_time in timestamps:
            # Random collection interval between 1 to 48 hours
            collection_interval = random.randint(1, 48)
            time_since_last = (current_time - last_collection_time).total_seconds() / 3600.0

            # Check if collection is needed
            if time_since_last >= collection_interval:
                last_collection_time = current_time
                time_until_next = 0  # Just collected
            else:
                time_until_next = collection_interval - time_since_last

            # Append data
            data.append([bin_id, current_time, current_time.hour, current_time.weekday(),
                        time_since_last, collection_interval, time_until_next])

    # Create DataFrame
    columns = ['Bin_ID', 'Timestamp', 'Hour_of_Day', 'Day_of_Week',
            'Time_Since_Last_Collection', 'Collection_Interval', 'Time_Until_Next_Collection']
    df = pd.DataFrame(data, columns=columns)
    return df

for i in range (1, 11):
    # Save to CSV
    df=create()
    file_path = './Model/DataFiles/bin_collection_data'
    df.to_csv(f"{file_path}{i}.csv", index=False)

