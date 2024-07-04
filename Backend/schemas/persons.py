from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime

class PersonBase(BaseModel):
    titulo_cortesia:str
    nombre:str
    primer_apellido:str
    segundo_apellido:str
    foto:str
    genero:str
    tipo_sangre:str
    fecha_nacimiento:datetime
    fecha_actualizacion:datetime
    created_at: datetime
    estatus: bool
    # Id_persona: int

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    id:int
    # owner_id: int clave foranea
    class Config:
        orm_mode = True
        