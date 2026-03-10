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
| Distro | [Void Linux](https://voidlinux.org/) |
| Wayland Compositor | [niri](https://github.com/niri-wm/niri) |
| Shell | [fish](https://fishshell.com/) |
| Prompt | [starship](https://starship.rs/) |
| System Shell / Panel | [Noctalia Shell](https://noctalia.dev/) |
| Terminal Emulator| [foot](https://codeberg.org/dnkl/foot) |

## 🚀 Installation

### 1) Install packages (Void Linux)

```bash
sudo xbps-install -S git stow
```

### 2) Clone

```bash
git clone https://github.com/dorpivovar/void-dotfiles.git ~/.dotfiles
cd ~/.dotfiles
```

### 3) Deploy

```bash
stow .
```
