from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base


class Estudiante(Base):
    __tablename__ = 'cancion'

    idEstudiante = Column(Integer, primary_key=True)
    apellPaterno = Column(String)
    apellMaterno = Column(String)
    nombre = Column(String)
    elegible = Column(Boolean)
