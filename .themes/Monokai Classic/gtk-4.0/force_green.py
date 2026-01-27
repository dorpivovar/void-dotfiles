import os

files = ["gtk.css", "gtk-dark.css"]

# Карта замен: ЧТО МЕНЯЕМ -> НА ЧТО (Зеленый Monokai)
color_map = {
    # --- ГЛАВНОЕ: Меняем Розовый на Зеленый ---
    "#F92672": "#A6E22E",  # Розовый HEX (UPPERCASE)
    "#f92672": "#a6e22e",  # Розовый HEX (lowercase)
    "249, 38, 114": "166, 226, 46", # Розовый RGB
    
    # Цвет при наведении (Розовый светлый -> Зеленый светлый)
    "#ff4d88": "#b7eb46", 
    
    # --- На случай, если где-то остался старый Бирюзовый ---
    "#7fbbb3": "#a6e22e",
    "127, 187, 179": "166, 226, 46",
    
    # --- Исправление цвета текста на кнопках ---
    # Иногда на зеленом фоне белый текст плохо читается,
    # в Monokai на зеленом часто используют темный текст.
    # Если хотите белый текст на кнопках, удалите следующую строку:
    # "accent_fg_color #F8F8F2": "accent_fg_color #272822", 
}

def convert_file(filename):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    # Читаем файл
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Заменяем
    for old, new in color_map.items():
        content = content.replace(old, new)

    # Принудительно меняем блок define-color для GTK4/Libadwaita
    # Это "жесткая" перезапись переменных, чтобы наверняка сработало
    replacements = [
        ("@define-color accent_bg_color #F92672;", "@define-color accent_bg_color #A6E22E;"),
        ("@define-color accent_color #F92672;", "@define-color accent_color #A6E22E;"),
        ("@define-color accent_bg_color #f92672;", "@define-color accent_bg_color #a6e22e;"),
        ("@define-color accent_color #f92672;", "@define-color accent_color #a6e22e;"),
    ]
    
    for old_line, new_line in replacements:
        content = content.replace(old_line, new_line)

    # Сохраняем
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Готово! {filename} перекрашен из розового в зеленый.")

# Запуск
for f in files:
    convert_file(f)