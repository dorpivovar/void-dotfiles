import os

# Файлы для обработки
files = ["gtk.css", "gtk-dark.css"]

# Карта цветов: СТАРЫЙ -> НОВЫЙ (Monokai Green Edition)
color_map = {
    # --- Основные цвета ---
    "#272e33": "#272822",  # Фон (Темно-серый)
    "#293136": "#272822",  # Фон списков
    "#fffbef": "#f8f8f2",  # Текст (Почти белый)
    
    # --- АКЦЕНТ ТЕПЕРЬ ЗЕЛЕНЫЙ ---
    "#7fbbb3": "#a6e22e",  # Был бирюзовый -> Стал Monokai Green
    "#90c4bd": "#b7eb46",  # Цвет при наведении (Чуть светлее зеленого)
    
    # --- Служебные цвета ---
    "#8da101": "#a6e22e",  # Успех (Тоже зеленый)
    "#dfa000": "#fd971f",  # Предупреждение (Оранжевый)
    "#f85552": "#f92672",  # Ошибка (Оставили Розовым, чтобы выделялась)
    
    # --- RGB версии (для прозрачности) ---
    
    # Фон (272e33 -> 272822)
    "39, 46, 51": "39, 40, 34",
    
    # Текст (fffbef -> f8f8f2)
    "255, 251, 239": "248, 248, 242",
    
    # Акцент (ЗЕЛЕНЫЙ RGB: 166, 226, 46)
    "127, 187, 179": "166, 226, 46",
    
    # Зеленый успех (тот же RGB)
    "141, 161, 1": "166, 226, 46",
    
    # Оранжевый
    "223, 160, 0": "253, 151, 31",
}

def convert_file(filename):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    # Делаем бэкап (если еще нет)
    if not os.path.exists(filename + ".original"):
        os.rename(filename, filename + ".original")
        print(f"Оригинал сохранен как {filename}.original")
    
    # Читаем из оригинала (чтобы можно было запускать скрипт много раз без ошибок)
    # Если оригинала нет (например, уже запустили прошлый скрипт), читаем .bak или текущий
    source_file = filename + ".original" if os.path.exists(filename + ".original") else filename

    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Заменяем цвета
    for old, new in color_map.items():
        content = content.replace(old, new)
        if old.startswith("#"):
            content = content.replace(old.upper(), new)

    # Записываем в основной файл
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Готово! {filename} теперь зеленый.")

# Запуск
for f in files:
    convert_file(f)