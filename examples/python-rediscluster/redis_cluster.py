# -*- coding: utf-8 -*-

import argparse


parser = argparse.ArgumentParser(description='redis lock', add_help=True)

parser.add_argument('--redis-host', default="127.0.0.1", help='redis hostname to connect to')
parser.add_argument('--redis-port', default=6379, help='redis port to connect to')

args = parser.parse_args()

from rediscluster import StrictRedisCluster
    
import redis


startup_nodes = [{"host": args.redis_host, "port": args.redis_port}]
r = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)

#r = redis.StrictRedis(host=args.redis_host, port=args.redis_port)

pipe = r.pipeline()
pipe.llen("lol")  # len of lock
result = pipe.execute()

print result

exit()
    
# from https://pypi.org/project/redis-py-cluster/





from hungry_hungry_hippos import HungryHungryHippos


hhh = HungryHungryHippos(host=args.redis_host, port=args.redis_port)


hhh = HungryHungryHippos(redis_client=rc)

# from here on out the rest is same as always