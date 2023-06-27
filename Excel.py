import win32com.client
import os
import datetime


"""
Данная функция выполняет выгрузку данных в Excel. В функцию передаются данные и те записываются в файл
_______
Документация по pywin32: https://mhammond.github.io/pywin32/
_______
Если необходимо изменить записываемые данные в excel, 
то в переменную data вносим или удаляем необходимые переменные
"""


def Excel(query, lemmas, otvet, opportunities):

    Excel = win32com.client.Dispatch("Excel.Application") #Призываем приложение Excel
    path = os.path.abspath('Report.xlsx') #Указываем путь и название таблицы
    wb = Excel.Workbooks.Open(path) #Присваем значение книги Excel
    
    Excel.Visible = 1 # делаем книгу видимой

    sheet = wb.ActiveSheet   # работаем с активной страницей
    date= datetime.datetime.now() # Узнаем нынешнее время
    data= (date, query, lemmas, otvet, opportunities) # Создаем переменную, где будут хранятся нужные нам значения

    sheet = wb.ActiveSheet # выбираем нужный лист

    # ищем первую пустую строку
    i = 1
    while i < 1000:
        # т.е. столбец постоянно 1, а строку мы ищем перебором
        val = sheet.Cells(i, 1).value
        if val == None:
            break
        i = i + 1
# когда мы нашли пустую строку
# нам в цикле нужно его заполнить
# данными из списка 
    k = 1
    for rec in data:
        sheet.Cells(i, k).value = rec
        k = k + 1

   
    wb.Save() #Сохраняем excel

