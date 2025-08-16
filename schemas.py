from pydantic import BaseModel, EmailStr

# -------------------------
# Request Schemas
# -------------------------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# -------------------------
# Response Schemas
# -------------------------
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # allows returning SQLAlchemy model objects directly

