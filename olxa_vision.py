import os
import time
import json

with open('settings.json') as s:
  set = json.load(s)
phone = set['phone']
pc = set['pc']

print("Запускаем" + phone['camera'] + " и делаем снимок...")
os.system("cd platform-tools && adb shell am start -n "  + phone['camera'])
time.sleep(6)

print("Копируем из папки " + phone['path'] + " в папку " + pc['path_photo_load'])
os.system("cd platform-tools && adb pull " + phone['path'] + " " + pc['path_photo_load'])

print("Удаляем все из папки " + phone['path'])
os.system("cd platform-tools && adb shell rm " + phone['path'] + "/*")

print("Готово!")

input('Нажмите Enter для выхода\n')