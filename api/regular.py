# coding: utf-8
import re

def remove_tags(text: str) -> str:
    """
    Убирает все HTML-теги из текста, обеспечивая правильные переносы строк.
    """
    text = re.sub(r'</p\s*>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</div\s*>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<a.*?>.*?</a>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = text.strip()
    return text