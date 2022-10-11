import redis 
from time import time


REDIS_HOST = 'redis-10264.c269.eu-west-1-3.ec2.cloud.redislabs.com'
REDIS_PORT = 10264
REDIS_USER = 'default'
REDIS_PASSWORD = 'Q1cYNhiPgFgV9DhQKlz2MjxqN6b7TnzC'

redis_client = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, username = REDIS_USER, password = REDIS_PASSWORD)
#redis_client.set("message", "hello world")
#print(f'is connected: {redis_client.ping()}')
#print(redis_client.get("message").decode()) # b means byte if we do not use .decode()
ts_in_s = time()
# but redis requires the timestamp in milliseconds
ts = ts_in_s*1000
redis_client.ts().add("temperature", ts, 25.6)
