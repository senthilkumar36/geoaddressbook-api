# GeoAddressBook API

A production-ready FastAPI-based Address Book application with geolocation filtering.

## Features

- Create, update, delete addresses
- SQLite database
- Coordinate validation
- Radius-based filtering using Haversine formula
- Logging
- Swagger documentation

## Setup

git clone <your-repo-link>
cd geoaddressbook

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload

## Swagger UI

http://127.0.0.1:8000/docs
