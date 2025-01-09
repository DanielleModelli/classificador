
__author__ = 'Matheus M.'

# Importa fonte de dados
import psycopg2
from pymongo import MongoClient

class DAConexaoFactory():

    # Define atributos privados

    def __init__(self):
        pass

    # Cria Factory para objetos
    def getConnect(self, typeDatabase):
        # Define conexão e fonte de dados
        con = None
        if typeDatabase == 'postgresql':
            try:
                con = psycopg2.connect(user="CopelAdmin",
                                            password="TCCCopelAWS",
                                            host="copelemergencia.cljaacljkggn.us-east-2.rds.amazonaws.com",
                                            port="5432",
                                            database="CopelEmergenciaDB")

            except (Exception, psycopg2.Error) as error:
                self.__erroCon = str(error)

        if typeDatabase == 'mongodb':
            client = MongoClient('mongodb://localhost:27017/')
            con = client['databaseCopel']['baseClassificada']

        return con

    # Retorna Erros
    def getError(self):
        return self.__erroCon
