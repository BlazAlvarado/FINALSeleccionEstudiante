import random

from src.modelo.estudiantes import Estudiante
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    #Crea la BD
    Base.metadata.create_all(engine)

    #Abre la sesión
    session = Session()

    #crear estudiantes
    estudiante1 = Estudiante(idEstudiante= 71500070, apellPaterno = "Balbin", apellMaterno="Urcuhuaranga",nombre="Fernando",elegible =1)
    estudiante2 = Estudiante(idEstudiante= 71500071, apellPaterno="Blaz ", apellMaterno="Alvarado", nombre="Cristian", elegible=1)
    estudiante3 = Estudiante(idEstudiante= 71500072,apellPaterno="Barrera ", apellMaterno="Huamanlazo", nombre="Miguel", elegible=1)
    estudiante4 = Estudiante(idEstudiante= 71500073,apellPaterno="Arancibia ", apellMaterno="Sedano", nombre="Joselin", elegible=1)
    estudiante5 = Estudiante(idEstudiante= 71500074,apellPaterno="Chavez ", apellMaterno="Pino", nombre="Maxwell", elegible=1)
    estudiantes=[estudiante1,estudiante2,estudiante3,estudiante4,estudiante5]
    aleatorio = random.choice(estudiantes)
    for i in range(1):
        session.add(aleatorio)
        session.commit()