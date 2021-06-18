# Introduction

SUPERHEROES is a learning project, providing basic out-of-the-box capabilities
for learners to build upon.

This project is a React+Python+Flask application, modified from https://github.com/EvolveU-FSD/c6-superheros to use a python server, made
of two processes:
   1. a Flask "server" providing API support for retrieving and submitting
   data from the backend
   1. a React "client" providing a web-based UI

## Environment variables
PYTHONPATH=server
FLASK_APP=server/server.py
DATABASE='./server/superheros.sqlite'
## Starting the Flask server

In a command shell (CMD, PowerShell, Terminal, etc.) run the commands:
1. `pip install -r requirements.txt`
2. `flask run`

The server is now running on port *5000*.

## Starting the React client

In a command shell run the commands:
1. `cd client`
1. `npm install`
1. `npm run start`

Your browser should open to `http://localhost:4444`.  The React development
system is running on port *4444*.
