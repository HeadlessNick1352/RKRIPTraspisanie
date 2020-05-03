import requests
import os
import time
from bs4 import BeautifulSoup

# Парсинг страницы колледжа, получение ссылки на файл
htmlDoc = requests.get("http://rgkript.ru/raspisanie-zanyatiy/")
soup = BeautifulSoup(htmlDoc.text, "lxml")
url = str(soup.find("table", width=600).find("a").get('href'))

# Создание рабочей папки, если она не существует
try:
    os.mkdir("C:\\RaspWorkDir\\")
except FileExistsError:
    time.sleep(1)

# Загрузка файла в папку
f = open("C:\\RaspWorkDir\\raspisanie.xls", "wb")
ufr = requests.get(url)
f.write(ufr.content)
f.close()

# Открытие
os.startfile("C:\\RaspWorkDir\\raspisanie.xls")
