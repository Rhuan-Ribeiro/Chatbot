from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests

psid = 'fwhEPJcEC6jkSE654uK1XDVMJsGFWL-GkzYnHcRvRVYejNX8udKWOymduuSmeWOEdWvXVg.'
psidts = 'sidts-CjIBPVxjSj5_f8ke6_FoDdnRmsQamPwZ81xKBcUPi3fg0viPfU1OOLlk4uqKuA78EQjvBRAA'
psidcc = 'ABTWhQF4rf6P14bw-azxqEU_yudAptP3qMkANixUQ9KJhQ5P2f-qKh_fYtvFkHIl_XN-aHfthg'

# cria um conjunto com os tokens autenticados
# para poder usar o board

tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc,
}

# cria o objeto bard para ser usado
bard = BardCookies(cookie_dict=tokenCookies)

# define as ações da API para receber
# os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        # pega os dados da requisição
        data = request.data

        print("data reveived:")
        print(data['question'])

        answer = bard.get_answer(data['question'])
        return Response(status=200, data=answer)
