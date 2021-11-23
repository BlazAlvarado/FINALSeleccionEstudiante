from src.modelo.estudiantes import Estudiantes
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()

    estudiante = session.query(Cancion).get(2)


    estudiante.minutos = 5
    cancion.segundos = 30
    cancion.compositor = "Pedro Pérez"
    cancion.interpretes.append(interprete)
    session.add(cancion)
    session.commit()

    session.close()

    idEstudiante = Column(Integer, primary_key=True)
    apellPaterno = Column(String)
    apellMaterno = Column(String)
    nombre = Column(String)
    elegible = Column(Integer)