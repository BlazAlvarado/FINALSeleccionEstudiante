from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Estudiantes(Base):
    __tablename__ = 'cancion'

    idEstudiante = Column(Integer, primary_key=True)
    apellPaterno = Column(String)
    apellMaterno = Column(String)
    nombre = Column(String)
    elegible = Column(Integer)
