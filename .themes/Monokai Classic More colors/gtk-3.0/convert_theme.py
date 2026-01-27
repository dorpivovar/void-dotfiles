import os

files = ["gtk.css", "gtk-dark.css"]

# Карта "Разнообразный Monokai"
color_map = {
    # Фон и текст
    "#272e33": "#272822", 
    "#fffbef": "#F8F8F2",
    
    # Распределяем роли:
    # 1. Основной акцент делаем ГОЛУБЫМ (он приятнее для глаз как основной)
    "#7fbbb3": "#66D9EF", 
    
    # 2. Успех и чекбоксы — ЗЕЛЕНЫМ
    "#8da101": "#A6E22E",
    
    # 3. Ошибки и важные кнопки — РОЗОВЫМ
    "#f85552": "#F92672",
    
    # 4. Предупреждения и слайдеры — ОРАНЖЕВЫМ
    "#dfa000": "#FD971F",
}

def apply_diverse_monokai(filename):
    if not os.path.exists(filename): return
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    for old, new in color_map.items():
        content = content.replace(old, new)
        content = content.replace(old.upper(), new)

    # Обновляем блок переменных в конце для GTK4/Libadwaita
    # Здесь мы вручную прописываем РАЗНЫЕ цвета для РАЗНЫХ ролей
    overrides = """
@define-color accent_bg_color #66D9EF;
@define-color accent_color #66D9EF;
@define-color accent_fg_color #272822;
@define-color destructive_bg_color #F92672;
@define-color destructive_color #F92672;
@define-color success_bg_color #A6E22E;
@define-color success_color #A6E22E;
@define-color warning_bg_color #FD971F;
@define-color warning_color #FD971F;
@define-color error_bg_color #F92672;
@define-color error_color #F92672;
@define-color window_bg_color #272822;
@define-color window_fg_color #F8F8F2;
@define-color view_bg_color #272822;
@define-color view_fg_color #F8F8F2;
"""
    # Удаляем старые определения, если они есть, и добавляем новые
    if "@define-color accent_bg_color" in content:
        # Упрощенно добавим в конец, CSS применит последние значения
        content += overrides

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Файл {filename} теперь по-настоящему разноцветный!")

for f in files:
    apply_diverse_monokai(f)