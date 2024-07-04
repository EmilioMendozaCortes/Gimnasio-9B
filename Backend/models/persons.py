from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, index=True)
    titulo_cortesia = Column(String(10), index=True)
    nombre = Column(String(50), index=True)
    primer_apellido = Column(String(50), index=True)
    segundo_apellido = Column(String(50), index=True)
    foto = Column(LONGTEXT)
    genero = Column(String(15), index=True)
    tipo_sangre = Column(String(5), index=True)
    fecha_nacimiento =Column(DateTime)
    fecha_actualizacion =Column(DateTime)
    estatus = Column(Boolean, index=False)
    created_at = Column(DateTime)
    # Id_persona = Column(Integer)
    # intems = relationship("Item", back_populates="owner") Clave foranea