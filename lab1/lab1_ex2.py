from sqlite3 import Timestamp
import psutil
from time import time, sleep
import uuid
from datetime import datetime


mac_id = hex(uuid.getnode())

while True:
    ts = time()
    battery_level = psutil.sensors_battery().percent
    #print(battery_level.percent)
    power_plugged = psutil.sensors_battery().power_plugged
    formatted_datetime = datetime.fromtimestamp(ts)
    #print(power_plugged)
    print(f'{str(formatted_datetime)} - {mac_id}: battery = {battery_level}')
    print(f'{str(formatted_datetime)} - {mac_id}: power_plugged = {power_plugged}')
    sleep(2)

