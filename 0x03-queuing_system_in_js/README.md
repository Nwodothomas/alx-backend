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

**.babelrc**

```json
{
  "presets": [
    "@babel/preset-env"
  ]
}


**and…**

Don't forget to run `$ npm install` when you have the `package.json`.

**0. Install a Redis instance (mandatory)**

1. Download, extract, and compile the latest stable Redis version (higher than 5.0.7) from [Redis Downloads](https://redis.io/download/):

```bash
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make

1. Start Redis in the background with the following command:

```bash
$ src/redis-server &


2. Make sure that the server is working by testing with:

```bash
$ src/redis-cli ping

You should receive the following response:

```plaintext
PONG

3. Using the Redis client, set the value "School" for the key "Holberton" with the following command:

```plaintext
127.0.0.1:[Port]> set Holberton School

The response should be "OK."


Verify that the value was set correctly:
127.0.0.1:[Port]> get Holberton
It should return "School."

To stop the server, find the process ID of the `redis-server` 
(you can use `ps` and `grep` for this):

$ kill [PID_OF_Redis_Server]

Copy the `dump.rdb` file from the `redis-5.0.7` directory into the root of the Queuing project.

**Requirements:**

- Running `get Holberton` in the Redis client should return "School."

**Repo:**

- GitHub repository: alx-backend
- Directory: 0x03-queuing_system_in_js
- Files: README.md, dump.rdb
