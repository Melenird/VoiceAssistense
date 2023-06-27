import VoiceMagic
import Answerina 
import Excel
import pyttsx3
import sqlite3 as sl
import DataBase

"""
Основополагающая система. Тут прописан весь путь голосового ассистента. 
Для корректной работы исходного кода необходимо установить необходимые библиотеки.
Для установки библиотеки необходимо будет в терминале прописать код сразу после названия библиотеки:
___________________
speech_recognition: pip install SpeechRecognition -Библиотека для распознавания речи
pymorphy3: pip install pymorphy3 -Библиотека для леммитизации
pyttsx3: pip install pyttsx3 -Библиотека для синтеза речи
pywin32: pip install pywin32 -Библиотека для работы с Microsoft Excel
___________________
Документация по pyttsx3: https://pyttsx3.readthedocs.io/en/latest/
___________________

Проект содержит 5 файлов:
___________________
main.py- основной файл. Для работы ассистента необходимо запускать этот файл
VoiceMagic.py- файл с функцией распознавания речи и лемматизации. В нем можно изменить настройки конфигурации микрофона
Answreina.py- файл с ответами. В нем можно изменить базу данных ответов и ключевых слов
Excel.py- файл для записи отчетности. В нем можно изменить настройки записываеммых данных
Report.xlsx- файл с записями отчетности
___________________
"""

engine=pyttsx3.init() #Присваиваем переменной класс для синтеза речи
def main():
    DataBase.DataBaseTagAndAnswer()
    #engine.say("Вас приветсвтует голосовой ассистент приемной комиссии ГУМРФ. Можете задать свой вопрос")
    #engine.runAndWait() #Воспроизводим речь ответа
    #query =VoiceMagic.listen_command() #получает текст голосового запроса
    biber='Когда будут известны списки поступивших'
    lemmas = VoiceMagic.lemmatize_text(biber) #Леммитизируем запрос
    print(lemmas) #Выводим полученные ключевые слова
    Keyword=', '.join(lemmas) #для записи в Excel
    request= set(lemmas) #Переводим леммизированные слова во множество
    Answerp= Answerina.poisk(request) #ищем ответ
    otvet= Answerina.Otvet(Answerp) #присваем ответ переменной 
    print (otvet) #Выводим ответ
    opportunities='нет'
    if Answerp !=0 :
        opportunities='да'
    DataBase.DataBaseReport(biber,Keyword, otvet, opportunities)
    engine.say(otvet) #Синтезируем речь ответа
    engine.runAndWait() #Воспроизводим речь ответа
    
    
    
if __name__ == '__main__':
    main()