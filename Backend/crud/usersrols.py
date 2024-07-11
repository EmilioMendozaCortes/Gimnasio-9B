import models.usersrols
import schemas.usersrols
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por id
def get_userrol(db:Session, id: int):
    return db.query(models.usersrols.UserRol).filter(models.usersrols.UserRol.Usuario_ID == id).first()

# Busqueda por rol
def get_userrol_by_user(db:Session, rol: int):
    return db.query(models.usersrols.UserRol).filter(models.usersrols.UserRol.Rol_ID == rol).first()

# Buscar todos los usuaurios-roless
def get_usersrols(db:Session, skip: int=0, limit:int=10):
    return db.query(models.usersrols.UserRol).offset(skip).limit(limit).all()

# Crear nuevo usuaurios-roles
def create_userrol(db:Session, userrol: schemas.usersrols.UserRolCreate):
    db_userrol = models.usersrols.UserRol(Usuario_ID=userrol.Usuario_ID, 
                                        Rol_ID=userrol.Rol_ID,
                                        Estatus=userrol.Estatus, 
                                        Fecha_Registro=userrol.Fecha_Registro, 
                                        Fecha_Actualizacion=userrol.Fecha_Actualizacion)
    db.add(db_userrol)
    db.commit()
    db.refresh(db_userrol)
    return db_userrol


# Eliminar un usuaurios-roles por id
def delete_userrol(db:Session, id:int):
    db_userrol = db.query(models.usersrols.UserRol).filter(models.usersrols.UserRol.Usuario_ID == id).first()
    if db_userrol:
        db.delete(db_userrol)
        db.commit()
    return db_userrol