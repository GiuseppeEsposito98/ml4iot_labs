from sqlite3 import Timestamp
import psutil
from time import time, sleep
import uuid
from datetime import datetime
import redis

REDIS_HOST = 'redis-10264.c269.eu-west-1-3.ec2.cloud.redislabs.com'
REDIS_PORT = 10264
REDIS_USER = 'default'
REDIS_PASSWORD = 'Q1cYNhiPgFgV9DhQKlz2MjxqN6b7TnzC'

mac_id = hex(uuid.getnode())
redis_client = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, username = REDIS_USER, password = REDIS_PASSWORD)

while True:
    ts = time()
    battery_level = psutil.sensors_battery().percent
    #print(battery_level.percent)
    power_plugged = psutil.sensors_battery().power_plugged
    formatted_datetime = datetime.fromtimestamp(ts)
    ts_in_s = ts*1000
    redis_client.ts().add("battery_level", ts, f'{str(formatted_datetime)} - {mac_id}: battery = {battery_level}')
    redis_client.ts().add("battery_level", ts, f'{str(formatted_datetime)} - {mac_id}: power_plugged = {power_plugged}')

    #print(power_plugged)
    print(f'{str(formatted_datetime)} - {mac_id}: battery = {battery_level}')
    print(f'{str(formatted_datetime)} - {mac_id}: power_plugged = {power_plugged}')
    sleep(2)