
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests, json

mockEnabled = True
mockedAnswear = '{"content": "Mengoo", "contentId": "383rufu3rhf"}'

psid = "g.a000gAhEPPHMVymwX2LTRa0QIf0HDfdKaA5iR57b9LfKNQb8jEHCr4PdUXuhaUP4XT2dG6wytwACgYKAbYSAQASFQHGX2Mi4JaDYnHOE4nbMCn9FF2elBoVAUF8yKrgYhvy_0Lsu9wJTxoD6yJ30076"
psidts = "sidts-CjIBPVxjSj_CPGt92tbnUDWigzP90YDU2OIHeWsLtORIPU-46mfKFuNMZuIdDkJxrgX2kBAA"
psidcc = "ABTWhQGgqVhkEvry6ZkmPaV3r7zymL3Euig9EopMfFES4A7BpxIHaoH3ubnSJrn1-KrWlfse"
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

