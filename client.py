import socket

lang = input('Please enter your language: ') #прописываем на каком языке мы будем писать

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #связываем сокет
client.connect(('localhost', 1337)) #прописываем наш хост и порт

while True: #наш цикл будет работать всегда
    message = input('Enter your message: ') #вводим сообщение которое нам нужно перевести

    if message == '!q': #выход из клиента
        client.close()
        break
    else:
        client.send(f'[{lang}]{message}'.encode()) #в ином случае нам выдаст наш язык и сообщение в расшифрованном виде