from pystrich.datamatrix import DataMatrixEncoder
import os
import base64


def generateDM(inputText):
    # Сначала принудительно удалим все файлы
    files_to_delete = os.listdir("static/Matrixes")
    for file_name in files_to_delete:
        file_path = os.path.join("static/Matrixes", file_name)
        os.remove(file_path)

    FNC1 = chr(231)  # 'ç'
    file_names = []
    for counter, data in enumerate(inputText, start=1):
        if is_base64(data):
            decoded_text = decode_base64_safe(data)
            if decoded_text is not None:
                data = FNC1 + decoded_text
            else:
                # Обработка недопустимой строки base64
                print("Строка не является действительным base64")
                continue
        else:
            data = FNC1 + data

        file_name = f"static/Matrixes/datamatrix_test{counter}.png"
        encoder = DataMatrixEncoder(data)
        file_names.append(file_name)
        encoder.save(file_name)

    # Получаем список имен файлов из папки
    file_names = os.listdir("static/Matrixes")
    # Создаем новый список, содержащий только имена файлов без пути
    file_names = [os.path.basename(file_name) for file_name in file_names]

    return file_names


def is_base64(s):
    try:
        decoded_bytes = base64.b64decode(s, validate=True)
        return True
    except (base64.binascii.Error, ValueError):
        return False


def decode_base64_safe(s):
    try:
        decoded_bytes = base64.b64decode(s)
        decoded_text = decoded_bytes.decode("utf-8")
        return decoded_text
    except (base64.binascii.Error, UnicodeDecodeError):
        return None


def getGtins(datamatrix_list):
    gtins = []
    for data in datamatrix_list:
        if is_base64(data):
            data = decode_base64_safe(data)
            if data is None:
                continue
        gtin = data[2:16]
        gtins.append(gtin)
    return gtins

