# Getting Started

This example shows how to make and catch a mutex lock.  The included script, mutex.py, does nothing
but create a lock, attempt to acquire it.  If it successfully aquires the lock it will do a 5 second countdown
before releaseing.  The other losing containers will wait until the lock has been released and then quit.

Run the commands below


```
docker-compose build
docker-compose up --scale handle=3
```

Only one of the three containers will successfully lock.

```
handle_1  | ['mutex.py']
handle_3  | ['mutex.py']
handle_2  | ['mutex.py']
handle_3  | Some other process already has a lock on list locks with value foo
handle_3  | Waiting for lock to be released
handle_1  | Successfully locked list locks with value foo
handle_2  | Some other process already has a lock on list locks with value foo
handle_2  | Waiting for lock to be released
handle_1  | During this time only this instance will operate on this given lock/value pair
handle_1  | Releasing lock in
handle_1  | 5
handle_1  | 4
handle_1  | 3
handle_1  | 2
handle_1  | 1
handle_1  | Done, releasing lock
handle_2  | Lock foo has been released
handle_2  | Quitting
handle_1  | Quitting
handle_3  | Lock foo has been released
handle_3  | Quitting
python-mutex_handle_3 exited with code 0
python-mutex_handle_2 exited with code 0
```



