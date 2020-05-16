from telegram.ext import Updater, CommandHandler

def main():
    updater = Updater(token="1146314119:AAEZfMFaiGupIVaSwhn9vKuyECx-U0XQWFE", use_context=True)

    #Añadiedo un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #Añadiedo un manejador al comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #Añadiedo un manejador al comando /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #Empezamos a pedir notificaciones a Telegram
    updater.start_polling()

    #Capturamos señales de parada
    updater.idle()

def start(update, context):
    #Responde al evento start con un texto fijo
    update.message.reply_text("Hola, soy un bot")

def repite(update, context):
    #Responde al mensaje con el mismo texto del mensaje recibido
    update.message.reply_text(update.message.text)

def suma(update, context):
    #args = [num1,num2] // Args son aquellos argumentos que esta recibiendo la funcion desde teelgram
    #Responde al mensaje con el mismo texto del mensaje recibido
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es %s" %(str(resultado)))

main()