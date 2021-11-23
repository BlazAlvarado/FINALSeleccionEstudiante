from src.modelo.estudiantes import Estudiante
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()

    estudiante1 = session.query(Estudiante).get(71500070)
    session.delete(estudiante1)

    session.commit()
    session.close()