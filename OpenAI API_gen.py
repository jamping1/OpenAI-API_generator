# Импортируем библиотеку для генерации (random)
import random  

# Импортируем библиотеку времени (для создания задержки)
import time

print(' ')

print('Генератор Бесплатных Ключей OpenAI API)!')

# Это задержка
time.sleep(0.9)  # время в секундах!!! 

print('......Генерация  Ключей OpenAI API......')

print('идёт OpenAI API генерация ключей не закрывать...')

print(' ')

time.sleep(0.8)  # время в секундах!!! 

print('......[ Идёт генерация ключей OpenAI API ]......')

print(' ')

chars = 'abcdefghijklnopqrstuvwxyz1234567890' 

number = input('◾ Укажите желаемое количество ключей для генерации:' + "\n")

print(' ')

length = input('◾Укажите длинну чека(обычно 40) (вводим 40):' + "\n")

print(' ')

number = int(number)
length = int(length)

print(' ')

print('ВНИМАНИЕ! Работа скрипта успешно завершена: ', number, ' ключей OpenAI API.')

print('ВНИМАНИЕ: Скрипт генерирует ключи OpenAI API, проверять на валидность придется вручную.либо купить чекер')

print('Автоматически чекер ключей OpenAI API можно купить у меня @fradyrad')

print(' ')

# Открываем файл для записи сгенерированных ссылок
with open('apikey.txt', 'w') as file:
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)

        # Генерируем ссылку
        link = 'sk-' + password
        
        # Печатаем сгенерированную ссылку на экран
        print(link)
        
        # Записываем сгенерированную ссылку в файл
        file.write(link + '\n')

print(' ')

print(' Удачного поиска!Воркеры :) ')

print()

toexit = input("Нажмите любую клавишу для завершения работы.")