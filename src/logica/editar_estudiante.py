from src.modelo.estudiantes import Estudiante
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()

    estudiante = session.query(Estudiante).get(1)


    estudiante.idEstudiante = 71500070
    estudiante.apellPaterno = "Blaz"
    estudiante.apellMaterno = "Balbin"
    estudiante.nombre = "Pedro "
    estudiante.elegible = 1
    session.add(estudiante)
    session.commit()
    session.close()