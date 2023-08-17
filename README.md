# Train Station API Service

Train Station API Service is a Django-based RESTful API for managing train stations, trips, orders, and more. It provides endpoints for creating, updating, and retrieving train-related data, as well as user registration and order management.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Introduction

Train Station API Service is designed to streamline the management of train-related data and user interactions. Whether you're developing a transportation app, building a train reservation system, or just exploring Django REST APIs, this project provides a solid foundation.

### Features:
- CRUD operations for trains, stations, routes, trips, and orders.
- Add images for trains
- Ticket validation based on cargo and seat availability.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/YKonoplyov/train-station-api-service.git
   ```
2. Create .env file and define environmental variables followin .env.example:
   ```
   POSTGRES_HOST= your db host
   POSTGRES_DB= name of your db
   POSTGRES_USER= username of your db user
   POSTGRES_PASSWORD= your db password
   SECRET_key=" your django secret key "
   ```
3. Run command:
   ```
   docker-compose up --build
   ```
4. App will be available at: ```127.0.0.1:8000```
5. Login using next credentials:
   ```
   admin@mail.com
   Agronom228
   ```
## Endpoints
    "train_types": "http://127.0.0.1:8000/api/train_station/train_types/",
    "trains": "http://127.0.0.1:8000/api/train_station/trains/",
    "stations": "http://127.0.0.1:8000/api/train_station/stations/",
    "routs": "http://127.0.0.1:8000/api/train_station/routs/",
    "trips": "http://127.0.0.1:8000/api/train_station/trips/",
    "crews": "http://127.0.0.1:8000/api/train_station/crews/"
    "documentatoin": "http://127.0.0.1:8000/api/schema/"
                     "http://127.0.0.1:8000/api/schema/swagger-ui/"
                     "http://127.0.0.1:8000/api/schema/redoc/ "

## Schema
![db_schema.png](images%2Fdb_schema.png)

## Screenshots
![swagger.png](images%2Fswagger.png)
![trip_list.png](images%2Ftrip_list.png)
![api_root.png](images%2Fapi_root.png)