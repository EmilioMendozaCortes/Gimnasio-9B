from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol

app = FastAPI()
app.include_router(user)
app.include_router(person)
app.include_router(rol)
print("Hola bienvenido a mi backend")