# ✨ dotfiles

**Void Linux + niri + Noctalia Shell** setup.

<p align="center">
  <img src="./assets/screenshots/preview-desktop.png" alt="Desktop preview" width="900" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Linux-Wayland-3b82f6?style=for-the-badge&logo=linux&logoColor=white" alt="Linux Wayland" />
  <img src="https://img.shields.io/badge/WM-niri-0f172a?style=for-the-badge" alt="niri" />
  <img src="https://img.shields.io/badge/Shell-fish-16a34a?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="fish" />
  <img src="https://img.shields.io/badge/Terminals-kitty%20%7C%20alacritty%20%7C%20foot-7c3aed?style=for-the-badge" alt="terminals" />
</p>

## 📸 Screenshots

<p align="center">
  <img src="./assets/screenshots/preview-terms.svg" alt="Terminals preview" width="49%" />
  <img src="./assets/screenshots/preview-shell.svg" alt="Shell preview" width="49%" />
</p>

## 📊 Program Mapping

| Category | Used |
| --- | --- |
| Distribution | Void Linux |
| WM / Compositor | niri |
| Shell | fish |
| Prompt | starship |
| System Shell / Panel | Noctalia Shell |
| Terminal (primary) | foot |
| Terminal (extra) | kitty, alacritty |
| System Monitoring | btop |
| System Info | fastfetch |
| Wayland Portals | xdg-desktop-portal |

## 🚀 Installation

### 1) Clone

```bash
git clone https://github.com/<your-username>/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
```

### 2) Install packages (Void Linux)

```bash
doas xbps-install -S git stow fish starship kitty alacritty foot btop fastfetch
```

### 3) Deploy

```bash
stow .
```

## 🗂 Structure

```text
.bash_profile
.config/
  alacritty/
  btop/
  fastfetch/
  fish/
  foot/
  kitty/
  niri/
  noctalia/
  xdg-desktop-portal/
.icons/
.themes/
assets/
  screenshots/
```

## ⚡ Useful Commands

- `ff` — run `fastfetch`
- `pon` / `poff` — enable/disable proxy
- `xi` / `xr` / `xu` / `xf` — quick `xbps` commands
- `conf-fish`, `conf-niri`, `conf-term` — quick access to key config files

## 🛠 Customization

- `kitty` theme: `.config/kitty/current-theme.conf`
- `alacritty` theme: `.config/alacritty/themes/noctalia.toml`
- Main WM config: `.config/niri/config.kdl`
- Main shell config: `.config/fish/config.fish`