import VoiceMagic
import pyttsx3
import sqlite3

"""
В файле содержатся функции, отвечающие за ответ
__________________________
Если необходимо увеличить базу данных вопросов, то необходимо:
1. Прописать в функции новую переменную для нового вопроса. 
Ее структура должна выглядеть следующим образом:
*Имя_Переменной*=len(request.intersection({*Ключевые слова через пробел и в одинарных кавычках*}))
2. Внести данную переменную в массив FAQ.
3. В словаре Otvet прописать новый номер ключа и ответ на вопрос. 
Пример:
*номер ключа* : "*ответ*"
_____________________
"""

#Функция выбора ответа из Базы данных в таблице TagAndAnswer
def Otvet(KeyAnswer):
    if KeyAnswer ==0: #Проверка возможности ответа
        return "Не могу ответить на ваш вопрос. Перевожу вас на оператора"
    sqlite_connection = sqlite3.connect('AbiturGumrf.db') #Вызываем базу данных
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT Answer FROM TagAndAnswer WHERE id = ?", (KeyAnswer, )) #Ищем правильный ответ из Базы данных
    result = cursor.fetchone()
    if result:
        return result[0] #Возвращаем результат
    
#Функция поиска ключа. Является основной функцией в данном файле
def poisk(request): 
    FAQ=Teg(request) # Формирование массива со значением совпавших множеств
    KeyAnswer=FoundAnswer(FAQ, request) #Поиск ключа среди наибольших совпавших значений
    if (KeyAnswer== 0): # Алгоритм переспроса вопроса, если было названо мало слов в множестве
        request=RepeatPlease(request) #Вызов функции 
        FAQ=Teg(request) #Формирование нового массива
        KeyAnswer=FoundAnswer(FAQ, request) # поиск нового ключа
    return KeyAnswer
            
#Функция создания массива колличества совпавших элементов с множеством запроса             
def Teg(request):
    sqlite_connection = sqlite3.connect('AbiturGumrf.db') #Вызываем базу данных
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from TagAndAnswer""" #Вызываем тэги из Базы данных
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall() 
    FAQ=[ n for n in records] #Формируем массив колличества совпавших элементов с множеством запроса
    for row in records:
        FAQ[row[0]-1]= len(request.intersection(set(row[1].split())))
    FAQ.insert(0, 1)
    return FAQ  

#Функция поиска лучшего совпадения. Чем больше совпавших значений, тем вероятнее ответ на вопрос
def FoundAnswer(FAQ, request):
    Answer = max(FAQ)
    AnswerIndex= FAQ. index (Answer) 
    FAQ.pop(AnswerIndex)
    for poiski in FAQ: #Алгоритма поиска наибольшего пересечения
        if FAQ[poiski] == Answer:
            AnswerIndex =0 
    return AnswerIndex

#Функция, которая вызывается, если программа не может ответить на вопрос. 
#Выполняет переспрашивание вопроса и увеличение множество запроса новыми данными.
def RepeatPlease(request):
    engine=pyttsx3.init()
    engine.say('Повторите свой вопрос')
    engine.runAndWait() #Воспроизводим речь ответа
    Biber=('У нотариуса')
    #query =VoiceMagic.listen_command() #Прослушивает новый запрос
    lemmas = VoiceMagic.lemmatize_text(Biber) #Леммитизируем запрос
    print(lemmas) #Выводим полученные ключевые слова
    newrequest= set(lemmas) #Переводим леммизированные слова во множество
    Itog= newrequest.union(request)
    return Itog