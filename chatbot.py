import time

#import openai
#importa lib telebot
import telebot

#armarzena chave api em uma variavel
chave_api = '6874563467:AAFobXagFci2sBX-nxMjIv3TIhWswiVT3eI'
#cria o bot sem as funcionalidades
bot = telebot.TeleBot(chave_api)

#@bot.message_handler(chat_types=mensagem.chat)
#def TesteCativo(mensagem):


@bot.message_handler(commands=["TesteCativo"])
def TesteCativo(mensagem):
    if len(mensagem.text) != 23:
        bot.send_message(mensagem.chat.id, "Informe o numero da telemedição no seguinte formato /TesteCativo 0000000000 ")
    msg = mensagem.text
    if len(mensagem.text) > 20:
        comando, nio = msg.split(" ")
        bot.send_message(mensagem.chat.id,"Aguarde Testando TM " + nio + " ....")
        time.sleep(5)
        bot.send_message(mensagem.chat.id,"Conectado 	Medidor: 44629040	03 canais	-76dB")
        print(nio)


@bot.message_handler(commands=["TrocaCativo"])
def TrocaCativo(mensagem):
    if len(mensagem.text) != 23:
        bot.send_message(mensagem.chat.id,
                         "Informe o numero da telemedição no seguinte formato /TrocaCativo 0000000000 ")
    msg = mensagem.text
    if len(mensagem.text) > 20:
        print("qualquercoisa")
        comando, nio = msg.split(" ")
        bot.send_message(mensagem.chat.id, "Aguarde Testando TM " + nio + " ....")
        time.sleep(5)
        bot.send_message(mensagem.chat.id, "Conectado 	Medidor: 44629040	03 canais	-76dB")


@bot.message_handler(commands=["TesteLivre"])
def TesteLivre(mensagem):
    pass

@bot.message_handler(commands=["TrocaLivre"])
def TrocaLivre(mensagem):
    pass

@bot.message_handler(commands=["Abraco"])
def Abraco(mensagem):
    print(mensagem)
    print(mensagem.chat.id)
    bot.send_message(mensagem.chat.id, "Valeu! Operador mandou abraço de volta!")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, """
    
    Escolha uma das opções para continuar (clique no item)
    
    /TesteCativo -  Consultar Nivel de sinal
    
    /TrocaCativo - Fazer Troca de Telemetria no Hemera
    
    /TesteLivre - Consulta nivel de sinal e parametros
    
    /TrocaLivre - Troca Telemetria
    
    /Abraco - Mandar um Abrço para o Operador do COM
    
    Atenção! comandos diferentes dos acima não vai funcionar! """)





bot.polling()
