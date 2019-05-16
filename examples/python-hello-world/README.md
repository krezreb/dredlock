# Getting Started


```
docker-compose build
docker-compose up --scale handle=3
```

In the above example we've spawed 3 handlers


Initial logs from docker

```
handle_1  | ['hello-world.py']
redis_1   | 1:M 31 Oct 15:02:53.756 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
redis_1   | 1:M 31 Oct 15:02:53.756 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
redis_1   | 1:M 31 Oct 15:02:53.756 * DB loaded from disk: 0.000 seconds
redis_1   | 1:M 31 Oct 15:02:53.756 * The server is now ready to accept connections on port 6379
handle_1  | connecting to redis
handle_1  | Entering while true loop, awaiting messages

```

Now feed a key and value into redis, in this case "foo" into the list "jobs"

```
docker-compose exec handle python push_to_redis.py jobs foo
```

Back in the docker logs we see that one and only one of our handlers got the message

```
handle_3  | Received value foo in list jobs
```




