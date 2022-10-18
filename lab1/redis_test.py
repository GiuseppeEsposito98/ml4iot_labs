import redis 
from time import time
from datetime import datetime


REDIS_HOST = 'redis-10264.c269.eu-west-1-3.ec2.cloud.redislabs.com'
REDIS_PORT = 10264
REDIS_USER = 'default'
REDIS_PASSWORD = 'Q1cYNhiPgFgV9DhQKlz2MjxqN6b7TnzC'

redis_client = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, username = REDIS_USER, password = REDIS_PASSWORD)
def safe_conn(value):
    try:
        redis_client.ts().create(value)
    except redis.ResponseError:
        pass
#redis_client.set("message", "hello world")
#print(f'is connected: {redis_client.ping()}')
#print(redis_client.get("message").decode()) # b means byte if we do not use .decode()
ts_in_s = time()
# but redis requires the timestamp in milliseconds
safe_conn('temperature')
ts = int(ts_in_s*1000)

redis_client.ts().add("temperature", ts, 25.6)

last_timestamp, last_value = redis_client.ts().get('temperature')
#print(last_timestamp)
#print(last_value)

#2022-10-18 14:30:00 -> timestamp
from_datetime = datetime.fromisoformat("2022-10-18 14:30:00")
from_timestamp_in_s = from_datetime.timestamp()
from_timestamp_in_ms = int(from_timestamp_in_s*1000) 

#2022-10-18 15:30:00 -> timestamp
to_datetime = datetime.fromisoformat("2022-10-18 15:30:00")
to_timestamp_in_s = to_datetime.timestamp()
to_timestamp_in_ms = int(to_timestamp_in_s*1000) 

values = redis_client.ts().range('temperature', from_timestamp_in_ms, to_timestamp_in_ms)
print(values)