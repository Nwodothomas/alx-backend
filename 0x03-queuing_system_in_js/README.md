# Solution to the 0x03. Queuing System in JS Tasks

## Required Technologies 

 Back-end JavaScript , ES6, Redis , NodeJS, ExpressJS, Kue

## Resources
   Read or watch:
1. [Redis Quick Start](https://redis.io/topics/quickstart)
2. [Redis Client Interface](https://redis.io/clients)
3. [Redis Client for Node.js](https://github.com/NodeRedis/node-redis)
4. [Kue (deprecated but still used in the industry)](https://github.com/Automattic/kue)

## Learning Objectives:
- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

## Requirements:

- All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All of your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the .js extension

## Required Files for the Project

### package.json

```json
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
        "lint": "./node_modules/.bin/eslint",
        "check-lint": "lint [0-9]*.js",
        "test": "./node_modules/.bin/mocha --require @babel/register --exit",
        "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
        "chai-http": "^4.3.0",
        "express": "^4.17.1",
        "kue": "^0.11.6",
        "redis": "^2.8.0"
    },
    "devDependencies": {
        "@babel/cli": "^7.8.0",
        "@babel/core": "^7.8.0",
        "@babel/node": "^7.8.0",
        "@babel/preset-env": "^7.8.2",
        "@babel/register": "^7.8.0",
        "eslint": "^6.4.0",
        "eslint-config-airbnb-base": "^14.0.0",
        "eslint-plugin-import": "^2.18.2",
        "eslint-plugin-jest": "^22.17.0",
        "nodemon": "^2.0.2",
        "chai": "^4.2.0",
        "mocha": "^6.2.2",
        "request": "^2.88.0",
        "sinon": "^7.5.0"
    }
}

### .babelrc

{
  "presets": [
    "@babel/preset-env"
  ]
}

To set up your project, don't forget to run the following command after creating the 
package.json file:

npm install


## Task 0: Install a Redis Instance

### Step 1: Download and Compile Redis

1. Download the latest stable Redis version (higher than 5.0.7) from [Redis Downloads](https://redis.io/download/):

   ```bash
   $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz

1. Extract the downloaded archive and navigate to the Redis directory:
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10

2. Compile Redis using the make command:
$ make


## Step 2: Start Redis Server

1. Start Redis in the background using the following command:
$ src/redis-server &


## Step 3: Check Redis Server Status
1. Ensure that the Redis server is running by pinging it using the Redis CLI:
$ src/redis-cli ping

If the server is running correctly, you will receive the response: PONG

## Step 4: Set and Retrieve Key-Value Pair
1. Using the Redis client, set the value "School" for the key "Holberton":
127.0.0.1:[Port]> set Holberton School

You should receive the response: OK

2. Retrieve the value associated with the "Holberton" key:
127.0.0.1:[Port]> get Holberton

You should receive the response: "School"

## Step 5: Kill Redis Server


1. To stop the Redis server, find the process ID (PID) of the redis-server process 
using ps and grep, and then use the kill command to terminate it:
$ ps aux | grep redis-server
$ kill [PID_OF_Redis_Server]

## Step 6: Copy dump.rdb

1. Copy the dump.rdb file from the redis-6.0.10 directory into the root of your 
Queuing project.

## Step 7: Verify Redis Configuration

1. Running get Holberton in the Redis client should return "School" if the 
configuration is correct.

This completes the installation and configuration of Redis for your Queuing project.


1. Node Redis Client
mandatory
Install node_redis using npm

Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:

It should log to the console the message Redis client connected to the server when the connection to Redis works correctly
It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work
Requirements:

To import the library, you need to use the keyword import
bob@dylan:~$ ps ax | grep redis-server
 2070 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-redis_client.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
bob@dylan:~$ 
bob@dylan:~$ ./src/redis-server > /dev/null 2>&1 &
[1] 2073
bob@dylan:~$ ps ax | grep redis-server
 2073 pts/0    Sl     0:00 ./src/redis-server *:6379
 2078 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
bob@dylan:~$
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 0-redis_client.js
