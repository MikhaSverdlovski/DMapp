import mysql.connector


def getFreeDM():

    # Подключение к базе данных
    cnx = mysql.connector.connect(user='root', password='adminadmin', host='localhost', database='DmAPP')

    # Создание курсора
    cursor = cnx.cursor()
    matrix = []
    try:
        cursor.execute("SELECT GTIN, customer, dmapp.matrix_status.Description, count(DISTINCT matrixcol) "
                       "FROM dmapp.matrix "
                       "join dmapp.matrix_status on dmapp.matrix.status = dmapp.matrix_status.id "
                       "group by GTIN, customer, dmapp.matrix_status.Description")
        result1 = cursor.fetchall()
        for res in result1:
            matrix.append(res)
        # Закрытие курсора
        cursor.close()

    except Exception as e:
        # Обработка ошибок
        print("Ошибка:", e)

    finally:
        # Закрытие соединения с базой данных
        cnx.close()

    return matrix

def get_gtin_description(gtin):
    # Подключение к базе данных
    cnx = mysql.connector.connect(user='root', password='adminadmin', host='localhost', database='DmAPP')

    # Создание курсора
    cursor = cnx.cursor()
    result = None  # Задаем значение по умолчанию
    try:
        # Ваш код для получения описания GTIN из таблицы gtindescr
        # Например, используя MySQL-запрос
        query = "SELECT descr " \
                "FROM gtinsdescr WHERE gtin = %s"
        cursor.execute(query, (gtin,))
        result = cursor.fetchone()
    except Exception as e:
        # Обработка ошибок
        print("Ошибка:", e)

    finally:
        # Закрытие соединения с базой данных
        cnx.close()

    if result:
        return result[0]
    else:
        return ""
