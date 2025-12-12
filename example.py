# coding: utf-8
from api.horo import HoroAPI

# User-Agent
user_agent = "" # ВСТАВЬТЕ СЮДА СВОЙ User-Agent

if not user_agent:
    user_agent = input("Введите User-Agent для парсера: ").strip()
    if not user_agent:
        print("User-Agent обязателен для работы парсера. Скрипт завершён.")
        exit(1)

# Инициализация парсера
horo = HoroAPI(user_agent)

# Словарь знаков зодиака: ключи — значения, используемые в API
zodiac_signs = {
    'aries': '♈️ Овен',
    'taurus': '♉ Телец',
    'gemini': '♊ Близнецы',
    'cancer': '♋️ Рак',
    'leo': '♌ Лев',
    'virgo': '♍ Дева',
    'libra': '♎ Весы',
    'scorpio': '♏ Скорпион',
    'sagittarius': '♐ Стрелец',
    'capricorn': '♑ Козерог',
    'aquarius': '♒ Водолей',
    'pisces': '♓ Рыбы'
}

# Словарь периодов: ключи — значения для API
period_map = {
    'yesterday': 'вчера',
    'today': 'сегодня',
    'tomorrow': 'завтра',
    'week': 'неделя',
    'month': 'месяц',
    'year': 'год'
}

# Пример: Гороскоп для конкретного знака
sign = 'cancer' # используем значение для API
date = 'today'  # используем значение для API

title, text = horo.get_horo(sign, date)
print(f"=== Гороскоп для {zodiac_signs[sign]} на {period_map[date]} ===")
print(title)
print(text)
print()

# Гороскоп на сегодня для всех знаков
title, text = horo.get_today_all()
print("=== Гороскоп на сегодня для всех знаков ===")
print(title)
print(text)
