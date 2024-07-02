from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(255), index=True)
    password = Column(LONGTEXT)
    created_at = Column(DateTime)
    estatus = Column(Boolean, index=False)
    Id_persona = Column(Integer)
    # intems = relationship("Item", back_populates="owner") Clave foranea