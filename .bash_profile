# .bash_profile

# Get the aliases and functions
[ -f $HOME/.bashrc ] && . $HOME/.bashrc

export XDG_CURRENT_DESKTOP=niri
export XDG_SESSION_DESKTOP=niri
export XDG_SESSION_TYPE=wayland

export MOZ_ENABLE_WAYLAND=1
export GDK_BACKEND=wayland,x11
export QT_QPA_PLATFORM="wayland;xcb"

export GTK_THEME=adw-gtk3
export QT_QPA_PLATFORMTHEME=qt6ct

if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
    exec dbus-run-session niri --session
fi
