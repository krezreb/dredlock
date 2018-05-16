# What the?

- Got a script that you want to be able to run multiple instances of in parallel?
- Want to write a program from scratch that's ready to scale up?

If so keep on readin'!

Hungry Hungry Hippos, (HHH) is a python implementation of redlock https://redis.io/topics/distlock with a set of examples that use docker, redis and docker compose.
The advantage of this approch, compared to multithreading, is that is can be applied in a single-threaded context (for example if you have to integrate existing code), scale across machines, handle dead lock recovery and require less adaptation of your existing code.

<img src="http://i.perezhilton.com/wp-content/uploads/2014/06/hungry-hippos.gif">

# Key concepts

- Process isolation
- Destributed locks (see https://redis.io/topics/distlock)
- Command orchestration

# Toolchain

- docker - images, containers, volumes
- docker-compose - building, linking services, scaling services
- redis - in memory key-value database


See examples for more fun