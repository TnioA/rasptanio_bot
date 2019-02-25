#-- coding: utf-8 --

import telepot

bot = telepot.Bot("603326028:AAEsLTP7tZi2r4Z77loCE562dsKK9MaFYbw")
def recebeMsg(msg):
    print(msg)
    ChatID = msg['chat']['id']
    
    if(msg['text'] == '/hello'):

        bot.sendMessage(ChatID, 'O que tu quer?')
    
    if(msg['text'] == '/time'):

        bot.sendMessage(ChatID, 'Não sou seu escravo')

    if(msg['text'] == '/news'):

        bot.sendMessage(ChatID, 'Vá se lascar, teu pai é outro')


bot.message_loop(recebeMsg)

print('Escutando')
while True:
    pass
