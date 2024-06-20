from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
users = []

# @userModel
class models_users(BaseModel):
    id:str
    usuarios:str
    contrasena:str
    created_at:datetime = datetime.now()
    estatus:bool=False

@user.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

@user.get('/users')
def get_usuarios():
    return users

@user.post('/users')
def save_users(insert_users:models_users):
    users.append(insert_users)
    print(users)
    return 'Datos guardados'