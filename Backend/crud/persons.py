import models.persons
import schemas.persons
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por ID
def get_person(db:Session, id: int):
    return db.query(models.persons.Person).filter(models.persons.Person.id == id).first()

# Busqueda por USUARIO
def get_person_by_usuario(db:Session, usuario: str):
    return db.query(models.persons.Person).filter(models.persons.Person.usuario == usuario).first()

# Buscar todos los usuarios
def get_persons(db:Session, skip: int=0, limit:int=10):
    return db.query(models.persons.Person).offset(skip).limit(limit).all()

# Crear nuevo usuario
def create_person(db:Session, user: schemas.persons.PersonCreate):
    db_person = models.persons.Person(usuario=user.usuario, password=user.password, created_at=user.created_at, estatus=user.estatus, Id_persona=user.Id_persona)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

# Actualizar un usuario por ID
def update_person(db:Session, id:int, user:schemas.persons.PersonUpdate):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.id == id).first()
    if db_person:
        for var, value in vars(user).items():
            setattr(db_person, var, value) if value else None
        db.commit()
        db.refresh(db_person)
    return db_person

# Eliminar un usuario por ID
def delete_person(db:Session, id:int):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.id == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person