from src.modelo.declarative_base import engine, Base, session
from src.modelo.estudiantes import Estudiante

class Coleccion():
    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_estudiante(self, idEstudiante,apellPaterno, apellMaterno, nombre, elegible):
        busqueda = session.query(Estudiante).filter(Estudiante.idEstudiante == idEstudiante).all()
        if len(busqueda) == 0:
            estudiante= Estudiante(idEstudiante= idEstudiante, apellPaterno = apellPaterno, apellMaterno=apellMaterno,nombre=nombre,elegible =elegible)
            session.add(estudiante)
            session.commit()
            return True
        else:
            return False



    def editar_estudiante(self, idEstudiante,apellPaterno, apellMaterno, nombre, elegible):
        busqueda = session.query(Estudiante).filter(Estudiante.idEstudiante ==idEstudiante) .all()
        if len(busqueda) == 0:
            estudiante = session.query(Estudiante).filter(Estudiante.id == idEstudiante).first()
            estudiante.idEstudiante = idEstudiante
            estudiante.apellPaterno = apellPaterno
            estudiante.apellMaterno = apellMaterno
            estudiante.nombre = nombre
            estudiante.elegible = elegible
            session.commit()

            return True
        else:
            return False

    def eliminar_estudiante(self, idEstudiante):
        try:
            estudiante= session.query(idEstudiante).filter(idEstudiante.id == idEstudiante).first()
            session.delete(estudiante)
            session.commit()
            return True
        except:
            return False