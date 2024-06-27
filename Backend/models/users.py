from sqlalchemy import Column,Boolean, Integer, String, DateTime
from config.db import Base

class users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(255), index=True)
    password= Column(String(255), index=True)
    estatus = Column(Boolean, index=True)