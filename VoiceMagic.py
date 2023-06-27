import speech_recognition
import pymorphy3

"""
Алгоритмы для прослушивания речи, преобразования его в речь,
а также прописан процесс лемматизации.
____________
Документация по библиотеке speech_recognition:  https://pypi.org/project/SpeechRecognition/
Документация по библиотеке pymorphy3: https://readthedocs.org/projects/pymorphy/downloads/pdf/v0.5.6/
____________
"""
sr = speech_recognition.Recognizer() #Подключаем класс для прослушивания

#Функция по распознования голоса и преобразовании его в текст 
def listen_command():
    try:
        with speech_recognition.Microphone() as mic:  #Работаем с микрофоном
            sr.adjust_for_ambient_noise(source=mic, duration=0.5) #Метод для учета шума
            audio = sr.listen(source=mic) #Запускам процесс прослушивания
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()  #распознаем голос, использую google API и переводим на русский
            
        return query
    except speech_recognition.UnknownValueError:
        return 0
    
#Функция по лемматизации распозновонного текста   
def lemmatize_text(query):
    # Создаем объект морфологического анализатора
    morph = pymorphy3.MorphAnalyzer()
    # Разбиваем текст на слова
    words = query.split()
    # Инициализируем массив для хранения лемматизированных слов
    lemmas = []
    # Проходимся по всем словам в тексте
    for word in words:
        # Получаем нормальную форму слова
        lemma = morph.parse(word)[0].normal_form
        # Добавляем лемматизированное слово в массив
        lemmas.append(lemma)
    # Возвращаем массив лемматизированных слов
    return lemmas