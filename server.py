import socket
from googletrans import Translator

translator = Translator() #вызываем нашу функцию из main
server_lang = 'en' #выбираем на какой язык переводить,по умолчанию стоит английский язык

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #связываем сокет
server.bind(('localhost', 1337)) #подключаемся к хосту и порту
server.listen() #сервер читает что мы отправим

client, addr = server.accept() #связывание адресса

while True:
    message = client.recv(1024).decode() #сообщение декодируется со стороны клиента
    lang = message[1:message.index(']')] #убираются ненужные скобки
    translation = translator.translate(
        message[message.index(']')+1:],
        src=lang, dest=server_lang
    ) #происходит перевод нашего текста

    print(translation.text) #выводится полученный результат