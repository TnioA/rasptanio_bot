#-- coding: utf-8 --
import urllib3.request  
import telepot
import json, requests

#API FAKE PARA TESTES
#jsonplaceholder.typicode.com


#API DE NOTICIAS BRASIL
url = 'https://newsapi.org/v2/top-headlines?sources=globo&pageSize=5&apiKey=f6fdb7cb0f2a497d92dbe719a29b197f'
#http = urllib3.PoolManager()
#resp = http.request('GET',url)
resp = requests.get(url)
conteudo = json.loads(resp.content)
#print(conteudo['articles'][0]['title'])

bot = telepot.Bot("603326028:AAEsLTP7tZi2r4Z77loCE562dsKK9MaFYbw")

def recebeMsg(msg):
    print(msg)
    ChatID = msg['chat']['id']
    
    if(msg['text'] == '/start'):
    
        bot.sendMessage(ChatID, 'Já to acordado! Tu tá cego por acaso?')
    
    elif(msg['text'] == '/hello'):

        bot.sendMessage(ChatID, 'O que tu quer?')

    elif(msg['text'] == '/comands'):
        cmd = ('Comandos: \n\n' + '/start = Para iniciar o Bot\n/hello = Para me chamar\n/comands = Para Listar comandos válidos\n/news = Para receber algumas noticias')
        bot.sendMessage(ChatID, cmd)

    
    elif(msg['text'] == '/time'):

        bot.sendMessage(ChatID, 'Não sou seu escravo')

    elif(msg['text'] == '/news'):
        msg_news = ''
        c = 1
        for cont in conteudo['articles']:
            msg_news = (msg_news + ('Noticia {}: \n'.format(c) + cont['title'] + '\n\n'))
            c = int(c) + 1
        bot.sendMessage(ChatID, msg_news)

    else:
        bot.sendMessage(ChatID, 'Comando não encontrado\nResponda /comands para receber a lista de comandos')

bot.message_loop(recebeMsg)

print('Escutando')
while True:
    pass
