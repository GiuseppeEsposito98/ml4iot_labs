import redis 
from time import time
from datetime import datetime
from time import sleep


REDIS_HOST = 'redis-10264.c269.eu-west-1-3.ec2.cloud.redislabs.com'
REDIS_PORT = 10264
REDIS_USER = 'default'
REDIS_PASSWORD = 'Q1cYNhiPgFgV9DhQKlz2MjxqN6b7TnzC'

redis_client = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, username = REDIS_USER, password = REDIS_PASSWORD)
def safe_conn(value):
    try:
        redis_client.ts().create(value, chunk_size = 128)
    except redis.ResponseError:
        pass
print(f"is connected: {redis_client.ping()}")
redis_client.delete('temperature')
#print(f"memory (bytes): {redis_client.ts().info('temperature').memory_usage}") # if we change the chunk size this value will change accordingly
#print(f"# samples: {redis_client.ts().info('temperature').total_sample}")
#print(f"# chunk: {redis_client.ts().info('temperature').chunk_count}")


for i in range(100):
    timestamp_ms = int(time()*1000)
    redis_client.ts().add("temperature", timestamp_ms, 25 + i // 50)
    sleep(0.1)

print(f"memory (bytes): {redis_client.ts().info('temperature').memory_usage}") # if we change the chunk size this value will change accordingly
print(f"# samples: {redis_client.ts().info('temperature').total_samples}")
print(f"# chunk: {redis_client.ts().info('temperature').chunk_count}")
redis_client.delete('temperature')

try:
    redis_client.ts().create("temperature_uncompressed", chunk_size = 128, compressed = False)
except redis.ResponseError:
    pass

for i in range(100):
    timestamp_ms = int(time()*1000)
    redis_client.ts().add("temperature_uncompressed", timestamp_ms, 25 + i // 50)
    sleep(0.1)

print(f"memory (bytes): {redis_client.ts().info('temperature_uncompressed').memory_usage}") # if we change the chunk size this value will change accordingly
print(f"# samples: {redis_client.ts().info('temperature_uncompressed').total_samples}")
print(f"# chunk: {redis_client.ts().info('temperature_uncompressed').chunk_count}")
redis_client.delete('temperature_uncompressed')
# retention
one_day_in_ms = 24*60*60*1000
try:
    redis_client.ts().alter("temperature_avg", chunk_size=128)
except redis.ResponseError:
    pass

# in this way we are mixing retention with aggregation
# retention will be applied only on newly created data
# so first of all we should first set the rule
bucket_duration_in_ms = 1000
redis_client.ts().createrule('temperature', 'temperature_avg', aggregation_type='avg', bucket_size_msec=bucket_duration_in_ms)

print(f"memory (bytes): {redis_client.ts().info('temperature_avg').memory_usage}") # if we change the chunk size this value will change accordingly
print(f"# samples: {redis_client.ts().info('temperature_avg').total_samples}")
print(f"# chunk: {redis_client.ts().info('temperature_avg').chunk_count}")