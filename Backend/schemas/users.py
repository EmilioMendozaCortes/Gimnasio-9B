from pydantic  import BaseModel

class UserBase(BaseModel):
    usuario:str
    password:str
    estatus: bool=False

class UserCreate(UserBase):
    pass

class User(UserBase):
    id:int
    class Config:
        orm_mode = True
        