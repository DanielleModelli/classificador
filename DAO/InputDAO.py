__author__ = 'Matheus Marquezin'


from Connection.DAConexaoFactory import DAConexaoFactory
from MODEL.Emergencias import Emergencias


class InputDAO():

     # Construtor da classe
    def __init__(self):
        self.__error = None
        self.__con = None

        try:
            # Cria Conexão com o Factory Method Pattern
            conexao = DAConexaoFactory()
            self.__con = conexao.getConnect('mongodb')
        except (Exception) as error:
            self.__error = str(error)

    # Retorna Erro
    def persistirDados(self, data):
        return self.__con.insert({'indexedList':data})

    # Retorna Erro
    def getErro(self):
        return self.__error