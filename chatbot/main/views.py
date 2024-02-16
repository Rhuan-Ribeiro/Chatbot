
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests, json

mockEnabled = True
mockedAnswear = '{"content":"Eu ainda sou um robô burro!", "contentId": "383rufu3rhf"}'

psid = "g.a000gghEPACF5fGl33bKfN0UQXptE08Gk1m82KeOe1zvZbLAMuAkFI5HgUQsljHOKEqCp-cYDwACgYKAa0SAQASFQHGX2Mi9zUo9T-8qjMT49aK7r10YRoVAUF8yKobrjzJWuMM0C0d-sgbaGVP0076"
psidts = "sidts-CjEBYfD7Z0Vrm4iGoheOBdiM12YEVxFQEFPoHMXaze4vmM_3L9foC_Z6FzHcdb-uzBgtEAA"
psidcc = "ABTWhQHo1yqtGqZY1ao_1rEyW1geAvjNEV6cy6FGurcvsMSKLc_EQ1ymRjwU8mya7g1769Z_lQ"
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}


#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        #se o mock estiver ativo ele retorna o status 201 e a data do mock
        if mockEnabled == True:
            return Response(status=201, data=json.loads(mockedAnswear))
        
        #cria o objeto bard para ser usado
        bard = BardCookies(cookie_dict=tokenCookies)
        #pega os dados que veio na requisição
        data = request.data

        #pega o dados da conversationId caso ele seja informado para mander a mesma conversa com o chatbot
        conversationId = data.get("conversationId")

        #verifica se o id da conversa foi recebido
        if(conversationId is not None):

            #informa o bard para responder na conversa desejada
            bard.conversation_id = conversationId
        else:
            bard.conversation_id = None
        
        answer = bard.get_answer(data['question'])

        return Response(status=201,data=answer)

