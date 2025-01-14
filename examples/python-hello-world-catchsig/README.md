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
Starting handle_1 ... done
Creating handle_2 ... 
Creating handle_3 ... 
Creating handle_2 ... done
Creating handle_3 ... done
```

Now scale down to 2, this will send a SIG 15 to instance number 3

```
docker-compose scale handle=2
```

```
handle-3  | Caught a signal 15, exiting
handle-3 exited with code 0
```

