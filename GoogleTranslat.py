from googletrans import Translator

def text_translator(text='Hello friend', src='en', dest='ru'): #создаем функци, где определяем наш перевод
    try: #определяем в функции переменные
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)

        return translation.text #возрвщаем наш текст
    except Exception as ex: #в случае ошибки передаем все наши ошибки в ex
        return ex #далее возвращаем нашу ошибку

def main():
    print(text_translator(text='Попов,удачи тебе на собеседовании', src='ru', dest='en')) #делаем вывод нашей
    # функции, в котором записываем произвольный текст, язык на котором он был написан, и на каком языке нам он нужен


if __name__=='__GoogleTranslat__': #запускаем программу при помощи этого
    main()