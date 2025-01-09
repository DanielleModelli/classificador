import re
import nltk
from DAO.EmergenciasDAO import EmergenciasDAO
from DAO.InputDAO import InputDAO
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import RSLPStemmer

class GeradorInputIndexado():

    # Define SQL
    __sql = "SELECT emer.ocorrencia,comp.descricao_comp,causa.descricao_causa, emer.defeito,emer.obs_equipe,emer.estado FROM public.emergencias emer INNER JOIN public.ava_componentes comp on emer.comp = comp.cod INNER JOIN public.ava_causas causa on emer.causa = causa.cod where estado != 'CANCELADO' LIMIT 3000;"

    def __init__(self):
          self.__listIndexed = []
          self.__listaDados = EmergenciasDAO().buscaEmergencias(self.__sql)

    def gerarVetorIndexado(self):

        for row in self.__listaDados:
            obs_equipe = re.sub(r'[^\w]', ' ', row.getObservacaoEquipe())
            obs_equipe = re.sub(r'[0-9]+', ' ', obs_equipe)
            for palavra in obs_equipe.split():
                if(palavra not in self.__listIndexed):
                    self.__listIndexed.append(palavra)

        return InputDAO().persistirDados(self.__listIndexed)
        
    def classificarBase(self):
        vetorPorcentagem = []
        for row in self.__listaDados:
            porcentagemTotal = 0
            stopWords = set(stopwords.words('portuguese') + list(punctuation))
            st = RSLPStemmer()

            componentes_sem_stopwords = []
            componentes = word_tokenize(row.getComponente().replace('/',' ').lower())
            componentes_sem_stopwords = [componente for componente in componentes if componente not in stopWords]
            compStm = []
            for item in componentes_sem_stopwords:
                compStm.append(st.stem(item))
            tamanhoComponentes = len(compStm)
            quantidadeRepetComponente = 0

            causas_sem_stopwords = []            
            causas = word_tokenize(row.getCausa().replace('/',' ').lower())
            causas_sem_stopwords = [causa for causa in causas if causa not in stopWords]
            causaStm = []
            for item in causas_sem_stopwords:
                causaStm.append(st.stem(item))
            tamanhoCausas = len(causaStm)
            quantidadeRepetCausa = 0
        
            porcentagemComp = 0
            porcentagemCausa = 0
            
            obs = ""
            if row.getObservacaoEquipe():
                obs = word_tokenize(row.getObservacaoEquipe().replace('/',' ').lower())
                obs_sem_stopwords = [] 
                obs_sem_stopwords = [o for o in obs if o not in stopWords]
                obsStm = []
                for item in obs_sem_stopwords:
                    obsStm.append(st.stem(item))
                    
            for comp in compStm:
                for item in obsStm:
                    if comp == item:
                        quantidadeRepetComponente = quantidadeRepetComponente + 1
            
            for causa in causaStm:
                for item in obsStm:
                    if causa == item:
                        quantidadeRepetCausa = quantidadeRepetCausa + 1

            if quantidadeRepetComponente == 0:
                porcentagemComp = 0
            else:
                porcentagemComp =  (quantidadeRepetComponente * 100) / tamanhoComponentes

            if quantidadeRepetCausa == 0:
                porcentagemCausa = 0
            else:
                porcentagemCausa = (quantidadeRepetCausa * 100) / tamanhoCausas

            porcentagemTotal = ((quantidadeRepetCausa + quantidadeRepetComponente) * 100) / (tamanhoCausas + tamanhoComponentes)
            vetorPorcentagem.append({"causa":causaStm,"componente":compStm,"porcentagem comp":porcentagemComp,"porcentagem causa":porcentagemCausa , "porcentagem total" : porcentagemTotal, "descricao" : obsStm})
        # return InputDAO().persistirDados(vetorPorcentagem)
        return vetorPorcentagem
