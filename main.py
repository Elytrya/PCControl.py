import discord #импорт дискорда и discord.py
from discord.ext import commands
import os #импорт библиотеки os. Она нужна для ввода команд перезагрузки и остановки пк
import time # импорт библиотеки time. Она нужна для расчитывания времени, и задержки между действиями
import datetime # Данная библиотека нужна для логов
import sys # импорт библиотеки sys. Она нужна для ввода команд перезагрузки и остановки пк
import platform # Данная библиотека нужна для сбора конфигураций пк и ввода команды >pc_info
import pyautogui # для скриншотов
import random
import string
import requests #для выполнения HTTP/HTTPS запросов
import webbrowser # для открытие вкладок в браузере

intents = discord.Intents.default()
intents.message_content = True




bot = commands.Bot(command_prefix='>', intents=intents)
bot.remove_command('help')
#команда остановки пк
@bot.command()
async def stop_pc(ctx, key_user):
    await ctx.message.delete()
    key = "stopprotocol123"
    if key_user == key:
        await ctx.send("Ключ безопасный верен.")
        await ctx.send("Проверка ключа безопасности...")
        await ctx.send("Останавливаю ПК.")
        await ctx.send("Засекаю таймер 2 минуты.")
        await ctx.send("Записываю логи о включении протокола остановки ПК")
        logs_done()
        print("ПРОИСХОДИТ ОСТАНОВКА ПК. ЕСЛИ ВЫ ХОТИТЕ ЕЕ ОТМЕНИТЬ: ЗАКРОЙТЕ КОНСОЛЬ!!!")
        time.sleep(60)
        os.system("shutdown /s /t 60")
    else:
        await ctx.send("Ключ безопасности неверный. Протокол защиты включен.")
        await ctx.send("Записываю логи о включении протокола защиты.")
        logs_falied()
        protect_protocol()

#протокол защиты

def protect_protocol():

    print("Включен протокол защиты")

    time.sleep(120)
    print("Функции бота разблокированы.")


@bot.command()
async def vk(ctx, key_user):
    await ctx.message.delete()
    key = "vk_protocol"
    if key_user == key:
        await ctx.send("Проверка ключа безопасности...")
        await ctx.send("Ключ верный.")

        await ctx.send("Записываю лог о включении протокола открытии ВК")
        logs_done()
        await ctx.send("Выполняю, сэр. Подождите.")
        session = requests.Session()
        response = session.get("https://vk.com/feed")
        if response.status_code == 200:
            print('Страница успешно открыта')
            webbrowser.open("https://vk.com/feed")
        else:
            print('Произошла ошибка при открытии страницы')
            await ctx.send("404 ошибка. Сервис недоступен.")
    else:
        await ctx.send("Ключ безопасности неверный. Протокол защиты включен.")
        await ctx.send("Записываю логи о включении протокола защиты.")
        logs_falied()
        protect_protocol()

@bot.command()
async def youtube(ctx, key_user):
    await ctx.message.delete()
    key = "youtubeprotocol123"
    if key_user == key:
        await ctx.send("Проверка ключа безопасности...")
        await ctx.send("Ключ верный.")

        await ctx.send("Записываю лог о включении протокола открытии Ютуба")
        logs_done()
        await ctx.send("Выполняю, сэр. Подождите.")
        session = requests.Session()
        response = session.get("https://www.youtube.com/")
        if response.status_code == 200:
            print('Страница успешно открыта')
            webbrowser.open("https://www.youtube.com/")
        else:
            print('Произошла ошибка при открытии страницы')
            await ctx.send("404 ошибка. Сервис недоступен.")
    else:
        await ctx.send("Ключ безопасности неверный. Протокол защиты включен.")
        await ctx.send("Записываю логи о включении протокола защиты.")
        logs_falied()
        protect_protocol()


@bot.command()
async def open_web(ctx, key_user, link):
    await ctx.message.delete()
    key = "open_web_key1234"
    if key_user == key:
        await ctx.send("Проверка ключа безопасности...")
        await ctx.send("Ключ верный.")

        await ctx.send("Записываю лог о включении протокола открытии ссылки")
        logs_done()
        await ctx.send("Выполняю, сэр. Подождите.")
        session = requests.Session()
        response = session.get(link)
        if response.status_code == 200:
            print('Страница успешно открыта')
            webbrowser.open(link)
        else:
            print('Произошла ошибка при открытии страницы')
            await ctx.send("404 ошибка. Сервис недоступен.")
    else:
        await ctx.send("Ключ безопасности неверный. Протокол защиты включен.")
        await ctx.send("Записываю логи о включении протокола защиты.")
        logs_falied()
        protect_protocol()
     
#команда рестарта пк
@bot.command()
async def restart_pc(ctx, key_user):

    await ctx.message.delete()
    key = "restartprotocol123"
    if key_user == key:
        await ctx.send("Ключ безопасный верен.")
        await ctx.send("Проверка ключа безопасности...")
        await ctx.send("Перезагружаю пк")
        await ctx.send("Засекаю таймер 2 минуты.")
        print("Протокол перезагрузки ПК включен.")
        await ctx.send("Записываю лог о включении протокола перезагрузки ПК..")
        logs_done()
        print("ПРОИСХОДИТ ПЕРЕЗАГРУЗКА ПК. ЕСЛИ ВЫ ХОТИТЕ ЕЕ ОТМЕНИТЬ: ЗАКРОЙТЕ КОНСОЛЬ!!!")
        time.sleep(60)
        os.system("shutdown /r")
    else:
        await ctx.send("Ключ безопасности неверный. Протокол защиты включен.")
        await ctx.send("Записываю логи о включении протокола защиты.")
        logs_falied()
        protect_protocol()

#github разработчика
@bot.command()
async def github(ctx):
    await ctx.send("GitHub разработчика данного бота: https://github.com/Akitilltka ")

@bot.command()
async def restart(ctx,key_user):
        await ctx.message.delete()
        key = "restartbotprotocol123"
        if key_user == key:
            print("Протокол перезагрузки бота включен.")
            await ctx.send("Записываю лог о включении протокола перезагрузки бота..")
            logs_done()
            await ctx.send("Перезагрузка...")
            time.sleep(5)
            
            python = sys.executable
            os.execl(python, python, * sys.argv)

        else:
            await ctx.send("Ключ не верен! Включаю протокол защиты.")
            await ctx.send("Записываю лог о включении протокола защиты ")
            logs_falied()
            protect_protocol()






@bot.command()
async def stop(ctx,key_user):
        await ctx.message.delete()
        key = "stopbotprotocol123"
        if key_user == key:
            print("Протокол остановки бота включен.")
            await ctx.send("Записываю логи...")
            logs_done()
            await ctx.send("Остановка...")
            exit()


        else:
            await ctx.send("Ключ не верен! Включаю протокол защиты.")
            await ctx.send("Записываю логи...")
            logs_falied()
            await ctx.send("Включаю протокол...")
            protect_protocol()

@bot.command()
async def screen_pc(ctx,key_user):
        await ctx.message.delete()
        key = "screenprotocol"
        if key_user == key:
            print("Протокол скриншота включен")
            await ctx.send("Записываю логи...")
            logs_done()
            await ctx.send("Выполняю протокол выполнения скриншота.")
            filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.png'  # Создает случайное имя файла
            pyautogui.screenshot(filename)  # Захватывает скриншот и сохраняет его в файл с именем, сгенерированным выше
            await ctx.send(f"Вот ваш скриншот, сэр.", file=discord.File(filename))  # Отправляет скриншот в чат
            print("Скриншот был успешно отправлен отправителю")
        else:
            await ctx.send("Ключ не верен! Включаю протокол защиты.")
            await ctx.send("Записываю логи...")
            logs_falied()
            await ctx.send("Включаю протокол...")
            protect_protocol()



#система логов
def logs_done(): #Этот лог записывается, когда человек успешно совершил команду
     print("Записываю логи...")
     logs_file = open("logs_done.txt", "w+")

     logs_file.write(f"[ИНФОРМАЦИЯ СИСТЕМЫ ЗАЩИТЫ]: В {datetime.datetime.today()} БЫЛА СОВЕРШЕННА КОМАНДА! ЕСЛИ ЭТО БЫЛИ НЕ ВЫ - СМЕНИТЕ КЛЮЧ БЕЗОПАСНОСТИ! \n ")
     logs_file.close()

def logs_falied():
     print("Записываю логи...")
     logs_file = open("logs_falied.txt", "w+")

     logs_file.write(f"[ИНФОРМАЦИЯ СИСТЕМЫ ЗАЩИТЫ]: В {datetime.datetime.today()} БЫЛА ПОПЫТКА СОВЕРШИТЬ КОМАНДУ!\n ")
     logs_file.close()
     


@bot.command()
async def help(ctx):
     await ctx.send(">github - Открывает информацию о GitHub разработчика \n >restart (ключ) - перезагружает бота \n >restart_pc (ключ) - перезагружает пк \n >stop (ключ) - останавливает бота \n >stop_pc (ключ) - останавливает ПК \n >pc_info - информация о пк \n >open_web (ключ) (ссылка) - открывает страницу на пк. \n >youtube - открывает ютуб на пк \n >vk - открывает вк на пк")


@bot.command()
async def pc_info(ctx):
        for item in platform.uname():
            print(item)
        my_system = platform.uname()
        await ctx.send(f"Информация о OC: \n OS: {my_system.system} {my_system.release} \n ID Процесса : {os.getpid()} \n Версия Python: {sys.version} \n Версия компилятора: {platform.python_compiler()} \n Информация о версии для MacOS {platform.mac_ver()} \n Версия библиотеки libc для Unix {platform.libc_ver()} \n Название ПК {platform.node()}\n ИНФОРМАЦИЯ О ПК \n Процессор: {my_system.processor} \n Machine: {my_system.machine} \n")





@bot.event
async def on_command_error(ctx, error):
    print('Ошибка команды:', error)















config = {
    'token': 'MTE4NTUyOTYwMTE3MTE0MDYyOA.GZITRv.wIAk1q1hwFmyW_FYwQ8AqdB1SvBYZvmNhZKjEw',
    'prefix': '>',
    
}
bot.run(config['token'])





















