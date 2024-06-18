from fastapi import APIRouter

user = APIRouter()

@user.get('/users')

def helloworld():
    return 'Hola  9B'