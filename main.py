from Sensor.logger import logging
from Sensor.exception import SensorException
from Sensor.utils import get_collection_as_dataframe
import sys, os

if __name__=='__main__':

     try:
          get_collection_as_dataframe(database_name="aps",collection_name="sensor")
     except Exception  as e:
          print(e)
