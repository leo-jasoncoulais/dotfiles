#!/bin/bash

if [[ $(dirname $(dirname "$(realpath "$BASH_SOURCE")")) != $HOME ]]; then
    echo "Please run this script from your home directory"
    exit 1
fi

# Install dependencies

sudo pacman -Syyu
sudo pacman -S --noconfirm zsh curl neofetch waybar rofi
# sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# echo 'export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH' >> ~/.zshrc

# Install dotfiles

ln -sf ~/dotfiles/waybar ~/.config/waybar
ln -sf ~/dotfiles/rofi ~/.config/rofi
ln -sf ~/dotfiles/hyprland ~/.config/hypr
ln -sf ~/dotfiles/neofetch ~/.config/neofetch

# Install scripts

ln -sf ~/dotfiles/scripts ~/.local/bin

# Install fonts

ln -sf ~/dotfiles/JetBrainsFonts /usr/share/fonts/JetBrainsFonts

# Complete

echo "Finished installing dotfiles"
echo "Please restart your shell to apply changes"
