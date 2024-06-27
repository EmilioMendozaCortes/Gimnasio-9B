from fastapi import APIRouter, Depends
import models, schemas
# from schemas import users
from cruds import crud
from sqlalchemy.orm import Session
from config.db import Base, SessionLocal, engine
# from models import users
# from typing import List
# from pydantic import BaseModel
# from datetime import datetime


user = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Ruta de bienvenida
@user.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

# Ruta para obtener todos los usuarios
@user.get('/users', response_model=list[schemas.users],tags=['Usuarios'])
def get_usuarios(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    users = crud.get_users(db,skip=skip, limit=limit)
    return users

# Ruta para agregar un nuevo usuario
# @user.post('/users', response_model=UserModel,tags=['Usuarios'])
# def save_users(insert_users: UserModel):
#     users.append(insert_users)
#     return insert_users

# # Ruta para buscar un usuario por ID
# @user.get('/users/{user_id}', response_model=UserModel,tags=['Usuarios'])
# def get_usuario_por_id(user_id: str):
#     for user in users:
#         if user.id == user_id:
#             return user
#     return {"error": "Usuario no encontrado"}

# # Ruta para modificar un usuario por ID
# @user.put('/users/{user_id}', response_model=UserModel,tags=['Usuarios'])
# def update_usuario(user_id: str, updated_user: UserModel):
#     for i, user in enumerate(users):
#         if user.id == user_id:
#             users[i] = updated_user
#             return updated_user
#     return {"error": "Usuario no encontrado para modificar"}

# # Ruta para eliminar un usuario por ID
# @user.delete('/users/{user_id}', response_model=UserModel,tags=['Usuarios'])
# def delete_usuario(user_id: str):
#     for i, user in enumerate(users):
#         if user.id == user_id:
#             deleted_user = users.pop(i)
#             return deleted_user
#     return {"error": "Usuario no encontrado"}
