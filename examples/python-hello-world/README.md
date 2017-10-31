# Getting Started


```
docker-compose build
docker-compose up
```

Initial logs from docker

```
handle_1  | ['hello-world.py']
redis_1   | 1:M 31 Oct 15:02:53.756 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
redis_1   | 1:M 31 Oct 15:02:53.756 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
redis_1   | 1:M 31 Oct 15:02:53.756 * DB loaded from disk: 0.000 seconds
redis_1   | 1:M 31 Oct 15:02:53.756 * The server is now ready to accept connections on port 6379
handle_1  | connecting to redis
handle_1  | while true
```

Now feed a key and value into redis, in this case "poo" into the list "jobs"

```
docker-compose exec handle python push_to_redis.py jobs poo
```

Back in the docker logs we see that our handle got the message

```
handle_1  | got a jobs poo
handle_1  | while true
```

Now let's scale up!

```
docker-compose scale handle=3
```

```
Starting hhhhelloworld_handle_1 ... done
Creating hhhhelloworld_handle_2 ... 
Creating hhhhelloworld_handle_3 ... 
Creating hhhhelloworld_handle_2 ... done
Creating hhhhelloworld_handle_3 ... done
```

```
docker-compose ps
```

```
         Name                       Command               State    Ports   
 --------------------------------------------------------------------------
hhhhelloworld_handle_1   python -u hello-world.py         Up               
hhhhelloworld_handle_2   python -u hello-world.py         Up               
hhhhelloworld_handle_3   python -u hello-world.py         Up               
hhhhelloworld_redis_1    docker-entrypoint.sh redis ...   Up      6379/tcp 
```


Feed more values into redis and watch which instance of handle receives it.




