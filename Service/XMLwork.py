import xml.etree.ElementTree as ET
import re

def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    dms = []

    for dm_element in root.findall('.//DM/code'):
        dm_text = dm_element.text.strip()
        dm_text = re.sub(r'\s+', '', dm_text)  # Удаление пробелов, переносов строк и других невидимых символов
        if dm_text:
            dms.append(dm_text)

    return dms

