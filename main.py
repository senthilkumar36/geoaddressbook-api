from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, schemas, crud
from .utils import calculate_distance

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GeoAddressBook API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/addresses/", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)

@app.get("/addresses/", response_model=list[schemas.AddressResponse])
def get_addresses(db: Session = Depends(get_db)):
    return crud.get_addresses(db)

@app.put("/addresses/{address_id}", response_model=schemas.AddressResponse)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    updated = crud.update_address(db, address_id, address)
    if not updated:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated

@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_address(db, address_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted successfully"}

@app.get("/addresses/nearby/")
def get_nearby_addresses(lat: float, lon: float, radius: float, db: Session = Depends(get_db)):
    addresses = crud.get_addresses(db)
    nearby = []

    for addr in addresses:
        distance = calculate_distance(lat, lon, addr.latitude, addr.longitude)
        if distance <= radius:
            nearby.append({
                "id": addr.id,
                "name": addr.name,
                "distance_km": round(distance, 2)
            })

    return nearby
