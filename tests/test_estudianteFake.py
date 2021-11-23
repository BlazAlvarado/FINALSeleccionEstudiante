import datetime
import unittest
import random

from faker import Faker

from src.modelo.estudiantes import Estudiante
from src.logica.coleccion_estudiante import *
from src.modelo.declarative_base import Session
from fake_providers import *

class estudianteTestCaseFake(unittest.TestCase):
    def setUp ( self ) :
        self.logica= Coleccion()
        self.session = Session ( )
        self.data_factory = Faker ( )

        # Generación de datos con libreria Faker
        self.data_factory.add_provider ( idEstudianteProvider)
        self.data_factory.add_provider(apellPaternoProvider)
        self.data_factory.add_provider(apellMaternoProvider)
        self.data_factory.add_provider(nombreProvider)
        self.data_factory.add_provider(elegibleProvider)


        self.data=[]
        self.estudiante=[]
        for i in range ( 0 ) :
            self.data.append(
                (
                    self.data_factory.unique.idEstudiante( ),
                    self.data_factory.apellPaterno ( ),
                    self.data_factory.apellMaterno ( ),
                    self.data_factory.nombre (),
                    self.data_factory.elegible ()
                )
            )
            self.estudiante.append(
                Estudiante(
                    idEstudiante = self.data[ -1 ][ 0 ] ,
                    apellPaterno = self.data[ -1 ][ 1 ] ,
                    apellMaterno  = self.data[ -1 ][ 2 ] ,
                    nombre = self.data[ -1 ][ 3 ] ,
                    elegible =self.data[ -1 ][ 4 ]
                )
            )
            self.session.add ( self.estudiante[ -1 ] )

        '''
            Persiste los objetos
            En este setUp no se cierra la sesión para usar
            los albumes en las pruebas
        '''
        self.session.commit ( )
        #self.session.close()

    def tearDown ( self ) :
        self.session = Session ( )

        busqueda_estudiante = self.session.query ( Estudiante ).all ( )
        for estudiante in busqueda_estudiante :
            self.session.delete ( estudiante )

        self.session.commit()
        self.session.close()

    def test_constructor ( self ) :
        for estudiante , dato in zip ( self.estudiante , self.data ) :
            self.assertEqual ( estudiante.idEstudiante , dato[ 0 ] )
            self.assertEqual ( estudiante.apellPaterno , dato[ 1 ] )
            self.assertEqual ( estudiante.apellMaterno , dato[ 2 ] )
            self.assertEqual ( estudiante.nombre , dato[ 3 ] )
            self.assertEqual(estudiante.elegible, dato[4])


    def test_agregar_estudiante(self):
        idEstudiante = self.data_factory.unique.idEstudiante()
        apellPaterno= self.data_factory.apellPaterno()
        apellMaterno = self.data_factory.apellMaterno()
        nombre = self.data_factory.nombre()
        elegible = self.data_factory.elegible()

        resultado = self.logica.agregar_estudiante(idEstudiante, apellPaterno, apellMaterno, nombre, elegible )

        self.assertEqual(resultado, True)