# coding: utf-8
import re

def remove_tags(text: str) -> str:
    """
    Убирает все HTML-теги из текста.

    Args:
        text (str): Текст с HTML.

    Returns:
        str: Чистый текст без тегов.
    """
    # Сначала удаляем ссылки <a>...</a> целиком
    text = re.sub(r'<a.*?>.*?</a>', '', text, flags=re.DOTALL)
    # Потом убираем все остальные теги
    return re.sub(r'<[^>]+>', '', text)
