# What the?

Got a script that you want to be able to run multiple instances of in parallel? If so you've come to the right place.

Hungry Hungry Hippos, (HHH) is a python library and set of examples that use docker, redis and docker compose to demonstrate this.
The advantage of this approche, compared to multithreading, is that is can be applied in a single-threaded context, thus requiring less adaptation of your existing code.

<img src="http://i.perezhilton.com/wp-content/uploads/2014/06/hungry-hippos.gif">

# Key concepts

- Process isolation
- Shared locks
- Command orchestration

# Toolchain

- docker - images, containers, volumes
- docker-compose - building, linking services, scaling services
- redis - in memory key-value database
