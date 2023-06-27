import sqlite3 as sl
import datetime

def DataBaseReport(query, lemmas, otvet, opportunities):
    bd= sl.connect('AbiturGumrf.db')
    cursor= bd.cursor()

    with bd:
        data = bd.execute("select count(*) from sqlite_master where type='table' and name='Report'")
        for row in data:
            # если таких таблиц нет
            if row[0] == 0:
                with bd:
                    bd.execute("""
                        CREATE TABLE Report (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            date TEXT,
                            querry TEXT,
                            lemmas TEXT,
                            Answer TEXT,
                            opportunities TEXT
                        );
                    """)
    # подготавливаем  запрос
    sql = 'INSERT INTO Report (date, querry, lemmas, answer, opportunities) values(?, ?, ?,?,?)'
    date= datetime.datetime.now() # Узнаем нынешнее время
    # указываем данные для запроса
    data = [
        (date, query, lemmas, otvet, opportunities)
    ]
    # добавляем запись в таблицу
    with bd:
        bd.executemany(sql, data)
    
    return 0

def DataBaseTagAndAnswer():
    bd= sl.connect('AbiturGumrf.db')
    cursor= bd.cursor()

    with bd:
        data = bd.execute("select count(*) from sqlite_master where type='table' and name='TagAndAnswer'")
        for row in data:
            # если таких таблиц нет
            if row[0] == 0:
                with bd:
                    bd.execute("""
                        CREATE TABLE TagAndAnswer (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            Tag TEXT,
                            Answer TEXT
                        );
                    """)
    return 0