from models.db import query

# response = query('CREATE TABLE superhero (id SERIAL PRIMARY KEY, name VARCHAR NOT NULL, alterego VARCHAR, sidekick VARCHAR, nickname VARCHAR)')
response = query('CREATE TABLE "user" (id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR)')


print(response)
