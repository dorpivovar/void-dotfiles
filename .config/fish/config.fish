# if status is-login
#     if test -z "$DISPLAY" -a (tty) = "/dev/tty1"
#         # Переменные для окружения
#         set -gx XDG_CURRENT_DESKTOP niri
#         set -gx XDG_SESSION_TYPE wayland
#                  # Переменные для тем Qt
#         set -gx QT_QPA_PLATFORMTHEME qt6ct
#         set -gx QT_QPA_PLATFORM wayland
         
#         # Запуск сессии
#         exec dbus-run-session niri --session
#     end
# end

### --- УПРАВЛЕНИЕ ПРОКСИ --- ###
# Замени адрес и порт на свои (например, 127.0.0.1:1080)
set -g proxy_url "http://127.0.0.1:8080" 

function proxy_on
    set -gx http_proxy $proxy_url
    set -gx https_proxy $proxy_url
    set -gx ftp_proxy $proxy_url
    set -gx all_proxy $proxy_url
    set -gx HTTP_PROXY $proxy_url
    set -gx HTTPS_PROXY $proxy_url
    set -gx FTP_PROXY $proxy_url
    set -gx ALL_PROXY $proxy_url
    echo "Прокси включен: $proxy_url"
end

function proxy_off
    set -e http_proxy
    set -e https_proxy
    set -e ftp_proxy
    set -e all_proxy
    set -e HTTP_PROXY
    set -e HTTPS_PROXY
    set -e FTP_PROXY
    set -e ALL_PROXY
    echo "Прокси выключен"
end

function chafa --description 'Вызов chafa с исправлением фантомных нажатий'
    # --polite on отключает агрессивный опрос терминала
    # --watch off предотвращает лишние прерывания
    # < /dev/null перенаправляет ввод, чтобы ответы терминала не попадали в буфер
    command chafa --polite on --watch off $argv < /dev/null
end

### --- ПСЕВДОНИМЫ И АББРЕВИАТУРЫ (ABBR) --- ###

# Системное инфо
abbr -a ff 'fastfetch'

# Прокси
abbr -a pon 'proxy_on'
abbr -a poff 'proxy_off'

# Управление пакетами (Void Linux)
abbr -a xi 'doas xbps-install -S'
abbr -a xr 'doas xbps-remove -R'
abbr -a xu 'doas xbps-install -Su'
abbr -a xf 'xbps-query -Rs' # Поиск пакетов
abbr -a xclean 'doas xbps-remove -Ro' # Полная очистка сирот

# Быстрый доступ к конфигам
abbr -a conf-fish 'nano ~/.config/fish/config.fish'
abbr -a conf-niri 'nano ~/.config/niri/config.kdl'
abbr -a conf-term 'nano ~/.config/kitty/kitty.conf'

abbr -a cat 'bat'

alias vim="nvim"

### --- ФУНКЦИИ --- ###

# Создать директорию и сразу зайти в нее
function mkcd
    mkdir -p $argv
    cd $argv
end

set fish_greeting # Убирает приветствие при запуске
# starship init fish | source
