
import psycopg2

__author__ = 'Matheus Marquezin'


from Connection.DAConexaoFactory import DAConexaoFactory
from MODEL.Emergencias import Emergencias


class EmergenciasDAO():

     # Construtor da classe
    def __init__(self):
        self.__error = None
        self.__con = None

        try:
            # Cria Conexão com o Factory Method Pattern
            conexao = DAConexaoFactory()
            self.__con = conexao.getConnect('postgresql')
        except (Exception, psycopg2.Error) as error:
            self.__error = str(error)

    # Metodo de Manipulação de dados
    def buscaEmergencias(self,sql):

        listEmergencias = []

        # Executa SQL
        try:
            cursor = self.__con.cursor()
            cursor.execute(sql)

            for row in cursor:
                # Cria instancia do objeto
                emergencias = Emergencias()

                emergencias.setId(row[0])
                emergencias.setComponente(row[1])
                emergencias.setCausa(row[2])
                emergencias.setDefeito(row[3])
                emergencias.setObservacaoEquipe(row[4])
                emergencias.setStatus(row[5])

                listEmergencias.append(emergencias)
                #listEmergencias.append("COMPONENTE : "+emergencias.getComponente()+" CAUSA : "+emergencias.getCausa())

        except (Exception, psycopg2.Error) as error:
            self.__error = str(error)

       
        # Retorna Objeto
        return listEmergencias

    # Retorna Erro
    def getErro(self):
        return self.__error
