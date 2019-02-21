# recom-eval-mock

This is a mockup for an evaluation solution of a recommender system.

## Run the mockup

### Required:
- Docker
- MacOS/Linux

1. Open terminal in the root directory of this project and execute (make sure that docker is running):

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

## Shut down the mockup

1. Press CTRL+C in Terminal and then type in the following command:

```
$ docker-compose down
```

## Comments

- For the pure evaluation issue it would be better to show the user one recommendation after the other instead of clicking through the brands.
- As a feature it would be nice if the user could change the order of the recommendations or delete brands from the recommended list if they dont have any similarity with the selected brand. If the user could give recommendations for better results in this way, this could help to improve the algorithm.
