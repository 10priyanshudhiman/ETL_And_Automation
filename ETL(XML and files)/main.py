import pandas as pd
import numpy as np
import glob             # this module helps in selecting files
import xml.etree.ElementTree as ET   # this module helps in processing xml files
from datetime import datetime

# x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group',
# 'Software Group', 'Design Team', 'Infrastructure'], 'Salary':[100000, 80000, 50000, 60000]}
#
# df = pd.DataFrame(x);
#
# print(df)
#
#
#
# print(df.loc[0:2,'ID':'Department'])

# arr1 = np.array([1,2,3])
# arr2 = np.array([2,3,4])
#
# arr3 = arr1+arr2
# print(arr3)
# arr3 = 2*arr3
# print(arr3)
# arr3 = arr1*arr2
# print(arr3)
# arr3 = np.dot(arr1,arr2)
# print(arr3)

# ETL first example
 # settings paths

tmpfile = "temp.tmp"       # file used to stored all extracted data
logfile = "logfile.txt"    #all event logs will be stored here
targetfile = "transformed_data.csv"  #files where transformed data is stored

#  Extraction begins
# CSV extraction

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

# JSON extraction

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines= True)
    return dataframe

# XML extraction

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name","height","weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = dataframe._append({"name":name,"height":height,"weight":weight},ignore_index=True)
    return dataframe

#Extract function

def extract():
            extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])  # create an empty data frame to hold extracted data

            # process all csv files
            for csvfile in glob.glob("*.csv"):
                extracted_data = extracted_data._append(extract_from_csv(csvfile), ignore_index=True)

            # process all json files
            for jsonfile in glob.glob("*.json"):
                extracted_data = extracted_data._append(extract_from_json(jsonfile), ignore_index=True)

            # process all xml files
            for xmlfile in glob.glob("*.xml"):
                extracted_data = extracted_data._append(extract_from_xml(xmlfile), ignore_index=True)

            return extracted_data

# here tranformation begins

def transform(data):
        # Convert height which is in inches to millimeter
        # Convert the datatype of the column into float
        # data.height = data.height.astype(float)
        # Convert inches to meters and round off to two decimals(one inch is 0.0254 meters)
        data['height'] = round(data.height * 0.0254, 2)

        # Convert weight which is in pounds to kilograms
        # Convert the datatype of the column into float
        # data.weight = data.weight.astype(float)
        # Convert pounds to kilograms and round off to two decimals(one pound is 0.45359237 kilograms)
        data['weight'] = round(data.weight * 0.45359237, 2)
        return data

# here loading begins

def load(targetfile,data_to_load):
    data_to_load.to_csv(targetfile)

# logging
def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')

#Running

log("ETL Job Started")

log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")
print(extracted_data)

log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")
transformed_data

log("Load phase Started")
load(targetfile,transformed_data)
log("Load phase Ended")

log("ETL Job Ended")





