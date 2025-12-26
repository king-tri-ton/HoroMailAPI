# coding: utf-8
from api.horo import HoroAPI, ZODIAC_SIGNS, PERIOD_MAP

# User-Agent
user_agent = ""  # ВСТАВЬТЕ СЮДА СВОЙ User-Agent

if not user_agent:
    user_agent = input("Введите User-Agent для парсера: ").strip()
    if not user_agent:
        print("User-Agent обязателен для работы парсера. Скрипт завершён.")
        exit(1)

# Инициализация парсера
horo = HoroAPI(user_agent)

# Создаём обратный словарь для периодов (русский -> английский)
period_map_reverse = {v: k for k, v in PERIOD_MAP.items()}

# Пример: Гороскоп для конкретного знака
sign = 'cancer'  # используем значение для API
date = 'today'   # используем значение для API

title, text = horo.get_horo(sign, date)
print(f"=== Гороскоп для {ZODIAC_SIGNS[sign]} на {PERIOD_MAP[date]} ===")
print(title)
print(text)
print()

# Гороскоп на сегодня для всех знаков
title, text = horo.get_today_all()
print("=== Гороскоп на сегодня для всех знаков ===")
print(title)
print(text)