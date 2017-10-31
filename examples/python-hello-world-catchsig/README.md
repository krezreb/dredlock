# Getting Started

This example shows how to catch a sigterm.  This happens, for example, when you scale down.


```
docker-compose build
docker-compose up
```

Scale up to 3

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

Now scale down to 2, this will send a SIG 15 to instance number 3

```
docker-compose scale handle=2
```

```
handle_3  | Whoa I just got told to quit.  Sir yes sir!
hhhhelloworldsig_handle_3 exited with code 0
```

It is possible that the sig will not be caught.  This happens, for example, if the script is stuck waiting for a blpop.  In this case there is no data loss since the worker wasn't busy anyway.

