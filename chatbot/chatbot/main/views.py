
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests, json

mockEnabled = True
mockedAnswear = '{"content": "Mengoo", "contentId": "383rufu3rhf"}'

psid = "nbMCn9FF2elBoVAUF8yKrgYhvy_0Lsu9wJTxoD6yJ30076"
psidts = "sidts-CjIBPVxjSkHipotyMsci9QuoP6PsvzkP5tOBmas1Ov49wczOHR5dAHgR3LKR7KWPUuRAmBAA"
psidcc = "ABTWhQEFPTfWFWZc8JFMHN9UdKDRlspH9bibxpUz9-GuSYAgdCS7quHKavZSbz7r2Z_8Um59"
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}
#cria o objeto bard para ser usado
bard = BardCookies(cookie_dict=tokenCookies)

#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        if mockEnabled == True:
            return Response(status=201, data=json.loads(mockedAnswear))
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

