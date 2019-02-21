# recom-eval-mock

This is a mockup for an evaluation solution of a recommender system.

# Run the mockup

## Required:
- Docker
- MacOS/Linux

1. In Terminal direct into the root directory and execute (make sure that docker is running):

```
$ docker-compose up
```

2. Wait until everything is set up. Wait for something like that:

```
backend_1   |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
frontend_1  | Starting up http-server, serving ./
frontend_1  | Available on:
frontend_1  |   http://127.0.0.1:8080
frontend_1  |   http://172.20.0.3:8080
```

3. Open Browser on http://localhost:8080

# Shut down the mockup

1. Press CTRL+C in Terminal and then type in the following command:

```
$ docker-compose down
```
