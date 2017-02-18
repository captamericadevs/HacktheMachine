import pandas as pd
import numpy as np
import datetime

def parse_full_date(row):
    try:
        date = datetime.datetime.strptime(row, "%Y-%m-%dT%H:%M:%S+00:00")
        time = row[11:18].split(":")
        date = date.replace(hour=int(time[0]), minute = int(time[1]), second = int(time[2]))
    except Exception:
        date = datetime.datetime(year=2017, month=5, day=17, hour=11, minute=00)
    return date

def parse_float(x):
    try:
        x = float(x)
    except Exception:
        x = 0
    return x

def checkDepth():
    print("")

def courseChange():
    print("")

def speedChange():
    print("")

def widthlengthCheck():
    print("")

def courseHeading():
    print("")
    
def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.    

    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    nm = 3447.8 * c
    return nm
    
pos_columns = ["mmsi", "heading", "latitude", "longitude", "nmea", "course", "type", "speed", "time stamp"]
stat_columns = ["mmsi", "ship_and_cargo_type", "destination", "length", "nmea", "imo", "type", "eta", "draught", "name", "width", "call_sign", "time stamp"]

posDataList = pd.read_csv("position.csv", names=pos_columns, encoding='ISO-8859-1')
statDataList = pd.read_csv("static.csv", names=stat_columns, encoding='ISO-8859-1')

posDataList["longitude"] = posDataList["longitude"].apply(parse_float)
posDataList["latitude"] = posDataList["latitude"].apply(parse_float)
posDataList["time stamp"] = posDataList["time stamp"].apply(parse_full_date)
statDataList["time stamp"] = statDataList["time stamp"].apply(parse_full_date)

grouped = pd.concat(g for _,g in posDataList.groupby("mmsi")) 
posDataList['time_diff'] = grouped['time stamp'].diff()
posDataList['distance'] = haversine_np(grouped.longitude.shift(), grouped.latitude.shift(), grouped.longitude.ix[1:], grouped.latitude.ix[1:])
posDataList = posDataList.sort_index(by=['mmsi', 'time stamp'])
posDataList.to_csv(path_or_buf="diffposition.csv", header=False)
