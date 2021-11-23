import random
import unittest
from datetime import datetime
from datetime import timedelta
from src.modelo.estudiantes import Estudiante
from faker import Faker
from faker.providers import BaseProvider

class idEstudianteProvider(BaseProvider):
    def idEstudiante (self):
        idEstudiante = [71500071,71500072,71500073,71500074,71500075 ]
        return random.choice(idEstudiante)

class apellPaternoProvider(BaseProvider):
    def apellPaterno (self):
        apellPaterno = ["Blaz" ,"Balbin","Barrera","Arancibia","Chavez" ]
        return random.choice(apellPaterno)


class apellMaternoProvider(BaseProvider):
    def apellMaterno (self):
        apellMaterno = ["Alvarado","Urcuhuaranga","Huamanlazo","Sedano","Pino" ]
        return random.choice(apellMaterno)

class nombreProvider(BaseProvider):
    def nombre (self):
        nombre = ["Cristian","Fernando","Miguel","Joselin","Maxwell" ]
        return random.choice(nombre)

class elegibleProvider(BaseProvider):
    def elegible(self):
        elegible=[True,True,False,False]
        return random.choice(elegible)