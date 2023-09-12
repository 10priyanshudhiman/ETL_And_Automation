import glob
import pandas as pd
from datetime import datetime

targetfile = "bank_market_cap_gbp.csv"
logfile = "logfile.txt"  # all event logs will be stored here


def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe


columns = ['Name', 'Market Cap (US$ Billion)']
dataframe = pd.DataFrame(columns)


def extract(data):
    for jsonfile in glob.glob("*.json"):
        if jsonfile == "bank_market_cap_1.json":
            data = extract_from_json(jsonfile)
    return data


df = pd.DataFrame()
for csvfile in glob.glob("*.csv"):
    if csvfile == "exchange_rates.csv":
        df = pd.read_csv(csvfile, index_col=0)

GBP_to_USD = df.loc['GBP', 'Rates']
print(GBP_to_USD)
exchange_rate = 1.0 / GBP_to_USD


def transform(data):
    # exchange rate from USD to GBP is the reverse of that value
    # although for the remainig values it will be their respective from USD divided by GBP
    for index in data.index:
        price = data.loc[index, 'Market Cap (US$ Billion)']
        new_rate = round(price * exchange_rate, 3)
        data.loc[index, 'Market Cap (US$ Billion)'] = new_rate

    new_column_name = 'Market Cap (GBP$ Billion)'
    data.rename(columns={'Market Cap (US$ Billion)': new_column_name}, inplace=True)
    return data


def load(targetfile, data_to_load):
    data_to_load.to_csv(targetfile, index=False)


def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt", "a") as f:
        f.write(timestamp + ',' + message + '\n')


# Running

log("ETL Job Started")

log("Extract phase Started")
extracted_data = extract(dataframe)
print(extracted_data.head())
log("Extract phase Ended")

log("Transform phase Started")
transformed_data = transform(extracted_data)
print(transformed_data.head())
log("Transform phase Ended")

log("Load phase Started")
load(targetfile,transformed_data)
log("Load phase Ended")
#
log("ETL Job Ended")
