import ijson
import json
import pandas as pd

files = {'a','b','c','d','e','f','g'}
pos_columns = ("heading", "latitude", "longitude", "nmea", "course", "type", "speed", "time stamp")
stat_columns = ("ship_and_cargo_type", "destination", "length", "nmea", "imo", "type", "eta", "draught", "name", "width", "call_sign", "time stamp")
posDataFrame = pd.DataFrame(columns=pos_columns)
statDataFrame = pd.DataFrame(columns=stat_columns)
    
for letter in files:
    filename = "HTM_AIS_Data\\NMEA_decoded_2017_01"+letter+".txt"
    with open(filename, "r") as f:
        for line in f:
            json_parsed = json.loads(line)
            if "heading" in json_parsed:
                try:
                    mmsi=json_parsed["mmsi"]
                except:
                    mmsi=""
                try:
                    heading=json_parsed["heading"]
                except:
                    heading=""
                try:
                    latitude=json_parsed["latitude"]
                except:
                    latitude=""
                try:
                    longitude=json_parsed["longitude"]
                except:
                    longitude=""
                try:
                    nmea=json_parsed["nmea"]
                except:
                    nmea=""
                try:
                    course=json_parsed["course"]
                except:
                    course=""
                try:
                    type=json_parsed["type"]
                except:
                    type=""
                try:
                    speed=json_parsed["speed"]
                except:
                    speed=""
                try:
                    timestamp=json_parsed["timestamp"]
                except:
                    timestamp=""
                posDataFrame.loc[mmsi] = (heading, latitude, longitude, nmea, course, type, speed, timestamp)
            else:
                try:
                    mmsi=json_parsed["mmsi"]
                except:
                    mmsi=""
                try:
                    ship_and_cargo=json_parsed["ship_and_cargo_type"]
                except:
                    ship_and_cargo=""
                try:
                    destination=json_parsed["destination"]
                except:
                    destination=""
                try:
                    length=json_parsed["length"]
                except:
                    length=""
                try:
                    nmea=json_parsed["nmea"]
                except:
                    nmea=""
                try:
                    imo=json_parsed["imo"]
                except:
                    imo=""
                try:
                    type=json_parsed["type"]
                except:
                    type=""
                try:
                    eta=json_parsed["eta"]
                except:
                    eta=""
                try:
                    draught=json_parsed["draught"]
                except:
                    draught=""
                try:
                    name=json_parsed["name"]
                except:
                    name=""
                try:
                    width=json_parsed["width"]
                except:
                    width=""
                try:
                    call_sign=json_parsed["call_sign"]
                except:
                    call_sign=""
                try:
                    timestamp=json_parsed["timestamp"]
                except:
                    timestamp=""
                statDataFrame.loc[mmsi] = (ship_and_cargo, destination, length, nmea, imo, type, eta, draught, name, width, call_sign, timestamp)
        posDataFrame.to_csv(path_or_buf="dfposition.csv", mode="a", header=False)
        statDataFrame.to_csv(path_or_buf="dfstatic.csv", mode="a", header=False)
posDataFrame.to_pickle("dfpos.pkl")
statDataFrame.to_pickle("dfstat.pkl")
