import VoiceMagic
import Answerina 
import Timer
import Excel
import pyttsx3

engine=pyttsx3.init()




def main():
    print("Можете говорить")
    Biber= "почта документы дистанционно"
    #query =VoiceMagic.listen_command()
    #print(query)
    lemmas = VoiceMagic.lemmatize_text(Biber) #Леммитизируем запрос
    print(lemmas) #Выводим полученные ключевые слова
    Keyword=', '.join(lemmas) #для записи в Excel
    request= set(lemmas) #Переводим леммизированные слова во множество
    Answerp= Answerina.poisk(request) #ищем ответ
    otvet= Answerina.Otvet[Answerp] #присваем ответ переменной 
    print (otvet) #Выводим ответ
    engine.say(otvet)
    engine.runAndWait()
    opportunities='нет'
    if Answerp !=0 :
        opportunities='да'
    Excel.Excel(Biber,Keyword, otvet, opportunities)
    
    
if __name__ == '__main__':
    main()