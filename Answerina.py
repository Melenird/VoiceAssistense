import VoiceMagic

Otvet={
    0: "Я не могу ответить на ваш вопрос",
    1: "Документы можно подать по почте, почтовый адрес направления документов, необходимых для поступления — 198035, г. Санкт-Петербург, ул. Двинская, д.5/7",
    2: "Копии документов заверять не нужно. Вы предоставляете простые ксерокопии.",
    3: "При подаче заявления о приеме в Университет необходимо предоставить: Заявление о приеме на обучение, на обработку персональных данных, ксерокопии документов удостоверяющих личность, страховое свидетельство и оригиналы документа об образовании, фотографии 3x4 и результаты прохождения медицинского осмотра",
    4: "Да, нужна. Подробнее можете узнать на сайте приемной комисии ГУМРФ",
    5: "Всем поступающим иногородним студентам предоставляется общежитие. Курсанты (плавсостав) проживают в экипажах, им предоставляется обмундирование и питание. Студенты (в том числе и обучающиеся на бюджете) оплачивают проживание в общежитии при заселении."
}



def poisk(request): #Функция поиска ключа
    FAQ=TegAnswer(request) # Формирование массива со значением совпавших множеств
    KeyAnswer=FoundAnswer(FAQ, request) #Поиск ключа среди наибольших совпавших значений
    while (KeyAnswer== 0): # Алгоритм переспроса вопроса, если было названо мало слов в множестве
        request=RepeatPlease(request) #Вызов функции 
        print (request)
        FAQ=TegAnswer(request) #Формирование нового массива
        KeyAnswer=FoundAnswer(FAQ, request) # поиск нового ключа
    return KeyAnswer
            
def TegAnswer(request):
    DontUnderstand=2 #Минимум должно быть 2 ключевых слова в запросе. Если их меньше, система просит либо повторить вопрос, либо направляет к оператору
    Post=len(request.intersection({'почта', 'документ', 'дистанционно'})) #Вбиваем ключевые слова и смотрим множества, которые получились
    Noterius=len(request.intersection({'нотариус', 'заверить', 'документ', 'паспорт'}))
    SubmissionOfDocuments= len(request.intersection({'подача', 'заявления', 'документ', 'поступление'}))
    MedKomissia= len(request.intersection({'справка', 'медицинская', 'документ', 'справка'}))
    Dormitory= len(request.intersection({'общежитие', 'заселяться', 'город'}))

    FAQ= [DontUnderstand, Post, Noterius,SubmissionOfDocuments,MedKomissia, Dormitory] #Создаем массив с вопросами
    return FAQ

def FoundAnswer(FAQ, request):
    p=0
    Answer=FAQ[0] #Изучаем количество пересеченных множество
    AnswerIndex=0 #Запоминаем индекс(чтобы потом дать ответ)
    for poiski in FAQ: #Алгоритма поиска наибольшего пересечения
        if FAQ[poiski]>=Answer:
            Answer=FAQ[poiski]
            AnswerIndex=poiski
    for poiski in FAQ: #Алгоритм нахождения индекса ключа
        if (poiski==AnswerIndex):
            p=poiski
    return p

def RepeatPlease(request):
    print('Повторите свой вопрос')
    query =VoiceMagic.listen_command() #Прослушивает новый запрос
    lemmas = VoiceMagic.lemmatize_text(query) #Леммитизируем запрос
    print(lemmas) #Выводим полученные ключевые слова
    newrequest= set(lemmas) #Переводим леммизированные слова во множество
    Itog= newrequest.union(request)
    return Itog