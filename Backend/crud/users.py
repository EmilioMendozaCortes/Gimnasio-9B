import models.users
import schemas.users
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por ID
def get_user(db:Session, id: int):
    return db.query(models.users.User).filter(models.users.User.id == id).first()

# Busqueda por USUARIO
def get_user_by_usuario(db:Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.usuario == usuario).first()

# Buscar todos los usuarios
def get_users(db:Session, skip: int=0, limit:int=10):
    return db.query(models.users.User).offset(skip).limit(limit).all()

# Crear nuevo usuario
def create_user(db:Session, user: schemas.users.UserCreate):
    db_user = models.users.User(usuario=user.usuario, password=user.password, created_at=user.created_at, estatus=user.estatus, Id_persona=user.Id_persona)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Actualizar un usuario por ID
def update_user(db:Session, id:int, user:schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

# Eliminar un usuario por ID
def delete_user(db:Session, id:int):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user