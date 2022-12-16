import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "shraddha_data_aps"
COLLECTION_NAME = "shraddha_collection_sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(df.shape)

    #convert dataframe to Json to dump records to mongodb
    df.reset_index(drop=True,inplace=True)
    
    #convert dataframe to json
    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])

    #insert records into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)