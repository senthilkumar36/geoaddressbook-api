from pydantic import BaseModel, Field
from datetime import datetime

class AddressBase(BaseModel):
    name: str = Field(..., min_length=2)
    street: str
    city: str
    state: str
    country: str
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

class AddressCreate(AddressBase):
    pass

class AddressUpdate(AddressBase):
    pass

class AddressResponse(AddressBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
