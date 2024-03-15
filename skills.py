import os, webbrowser, sys, subprocess, pyttsx3
import voice
try:
    import requests
except:
    pass

#Открывает браузер по уполчанию с указанным url
def browser():
    webbrowser.open('https://www.youtube.com', new=2)

#запуск игры через его exe файл
def game():
    try:
        subprocess.Popen('C:\Program Files\Genshin Impact\launcher.exe')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')

#отлючение ПК с ОС windows
def offpc():
    # os.system('shutdown')
    print('пк выключен')

#данные взяты с сайта https://openweathermap.org
#для работы нужна регистрация на сайте
def weather():
    try:
        params = {'q': 'London', 'units': 'metric', 'lang': 'ru', 'appid': 'ключ к API'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')

#отключение бота
def offBot():
    sys.exit()

#заглушка
def passive():
    pass
