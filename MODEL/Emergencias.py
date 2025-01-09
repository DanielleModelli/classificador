
__author__ = 'Matheus Marquezin'
 
class Emergencias():
 
    # Define atributos privados
    def __init__(self):
        self.__id = None
        self.__componente = None
        self.__causa = None
        self.__defeito = None
        self.__obs_equipe = None
        self.__status = None
 
    # Define métodos Getter e Setter
    # Você também pode optar por propriedades
    def getId(self):
        return self.__id
 
    def setId(self, id):
        self.__id = id
 
    def getComponente(self):
        return self.__componente
 
    def setComponente(self, componente):
        self.__componente = componente
 
    def getCausa(self):
        return self.__causa
 
    def setCausa(self, causa):
        self.__causa = causa
 
    def getDefeito(self):
        return self.__defeito
 
    def setDefeito(self, defeito):
        self.__defeito = defeito
 
    def getObservacaoEquipe(self):
        return self.__obs_equipe
 
    def setObservacaoEquipe(self, obs_equipe):
        self.__obs_equipe = obs_equipe

    def getStatus(self):
        return self.__status
 
    def setStatus(self, status):
        self.__status = status


    def toString(self):
        stringRetorno = "{\n   id: "
        if self.__id:
            stringRetorno += self.__id
        else:
            stringRetorno += "''"
        stringRetorno += ", \n   componente: "
        if self.__componente:
            stringRetorno += self.__componente
        else:
            stringRetorno += "''"
        stringRetorno += ", \n   causa: "
        if self.__causa:
            stringRetorno += self.__causa
        else:
            stringRetorno += "''"
        stringRetorno += ", \n   defeito: "
        if self.__defeito:
            stringRetorno += self.__defeito
        else:
            stringRetorno += "''"
        stringRetorno += ", \n   obs_equipe: "
        if self.__obs_equipe:
            stringRetorno += self.__obs_equipe
        else:
            stringRetorno += "''"
        stringRetorno += ", \n   status: "
        if self.__status:
            stringRetorno += self.__status

        stringRetorno += "\n}"
        return stringRetorno
