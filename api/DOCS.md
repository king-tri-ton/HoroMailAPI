# HoroAPI Documentation

## Класс `HoroAPI`

Парсер гороскопов с сайта [horo.mail.ru](https://horo.mail.ru/).
Возвращает **заголовок и очищенный текст** (HTML-теги и ссылки `<a>` удаляются).

### Инициализация

```python
from api.horo import HoroAPI

# ВСТАВЬТЕ СВОЙ User-Agent
user_agent = ""  
if not user_agent:
    user_agent = input("Введите User-Agent для парсера: ").strip()

horo = HoroAPI(user_agent)
```

* **user_agent** (str): User-Agent для HTTP-запросов. Обязателен.

---

### Методы

#### `fetch_page(url: str) -> tuple[str, str]`

Возвращает заголовок и текст гороскопа с указанной страницы.

* **url**: полная ссылка на страницу гороскопа.
* **Возвращает**: `(title, text)` — заголовок и очищенный текст.

#### `get_today_all() -> tuple[str, str]`

Гороскоп на сегодня для всех знаков.

* **Возвращает**: `(title, text)`.

#### `get_horo(sign: str, date: str) -> tuple[str, str]`

Гороскоп для конкретного знака и периода.

* **sign**: знак зодиака (значение для API, например `cancer`, `aries`).
* **date**: период (значение для API, например `today`, `week`).
* **Возвращает**: `(title, text)`.

---

### Значения знаков и периодов

В модуле `api.horo` определены готовые словари, которые можно использовать напрямую.

#### Знаки зодиака

```python
from api.horo import ZODIAC_SIGNS

ZODIAC_SIGNS = {
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
````

#### Периоды

```python
from api.horo import PERIOD_MAP

PERIOD_MAP = {
    'вчера': 'yesterday',
    'сегодня': 'today',
    'завтра': 'tomorrow',
    'неделя': 'week',
    'месяц': 'month',
    'год': 'year'
}
```

---

### Примеры использования

```python
from api.horo import HoroAPI, ZODIAC_SIGNS, PERIOD_MAP

user_agent = input("Введите User-Agent: ").strip()
horo = HoroAPI(user_agent)

sign = 'cancer'
period = 'today'

title, text = horo.get_horo(sign, period)
print(f"Гороскоп для {ZODIAC_SIGNS[sign]} на {period}")
print(title)
print(text)
```

---

> Разработал [King Triton](https://github.com/king-tri-ton/)
