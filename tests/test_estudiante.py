from faker import Faker
import random
import unittest
from src.logica.coleccion_estudiante import Coleccion
from src.modelo.estudiantes import Estudiante
from src.modelo.declarative_base import Session

class EstudianteTestCase(unittest.TestCase):
    def setUp(self):
        '''Crea una colección para hacer las pruebas'''
        self.coleccion = Coleccion()

        '''Abre la sesión'''
        self.session = Session()

        '''Crea una instance de Faker'''
        self.data_factory = Faker ( )

        '''Se programa para que Faker cree los mismos datos cuando se ejecuta'''
        Faker.seed ( 1000 )

        '''Genera 10 datos en data y creamos los álbumes'''
        self.data = [ ]
        self.estudiante = [ ]
        for i in range ( 0, 4 ) :
            self.data.append((
                self.data_factory.text(),
                self.data_factory.text(),
                self.data_factory.text(),
                self.data_factory.text(),
                self.data_factory.boolean()))
            self.estudiante.append (
                Estudiante(
                    idEstudiante=self.data[ -1 ][ 0 ] ,
                    apellPaterno = self.data[ -1 ][ 1 ] ,
                    apellMaterno = self.data[ -1 ][ 2 ] ,
                    nombre = self.data[ -1 ][ 3 ] ,
                    elegible = self.data[ -1 ][ 4 ]

                ) )
            self.session.add ( self.estudiante[ -1 ] )

        '''Persiste los objetos
        En este setUp no se cierra la sesión para usar los albumes en las pruebas'''
        self.session.commit ( )

    def tearDown(self) :
        self.session = Session ( )
        busqueda = self.session.query ( Estudiante ).all ( )

        for estudiante in busqueda :
            self.session.delete ( estudiante )

        self.session.commit ( )
        self.session.close ( )

    def test_constructor(self):
        for estudiantes, dato in zip(self.estudiante, self.data):
            self.assertEqual(estudiantes.idEstudiante, dato[0])
            self.assertEqual(estudiantes.apellPaterno, dato[1])
            self.assertEqual(estudiantes.apellMaterno, dato[2])
            self.assertEqual(estudiantes.nombre, dato[3])
            self.assertEqual(estudiantes.elegible, dato[4])

    def test_agregar_estudiante ( self ) :
        '''Prueba la adición de un álbum'''
        self.data.append((
            self.data_factory.text(),
            self.data_factory.text(),
            self.data_factory.text(),
            self.data_factory.text(),
            self.data_factory.boolean()))
        resultado = self.coleccion.agregar_estudiante (
            idEstudiante=self.data[-1][0],
            apellPaterno=self.data[-1][1],
            apellMaterno=self.data[-1][2],
            nombre=self.data[-1][3],
            elegible=self.data[-1][4])
        self.assertEqual ( resultado , True )