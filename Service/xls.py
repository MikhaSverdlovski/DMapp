import openpyxl
import mysql.connector


# Пока оставлю мало ли надо будет чет загрузить еще
# Подключение к базе данных
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="adminadmin",
    database="dmapp"
)

# Открытие файла Excel
workbook = openpyxl.load_workbook(r'C:\Users\misha\ean11.XLSX')

sheet = workbook.active

# Чтение данных из файла и запись в базу данных
cursor = db.cursor()
for row in sheet.iter_rows(min_row=2, values_only=True):  # Пропускаем заголовки, начинаем со второй строки
    descr = row[0]
    gtin = row[1]
    cursor.execute("INSERT INTO gtinsdescr (descr, gtin) VALUES (%s, %s)", (descr, gtin))
    db.commit()

# Закрытие подключения к базе данных
cursor.close()
db.close()
